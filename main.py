import os
import argparse
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content  
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from dotenv import load_dotenv
from google import genai
from google.genai import types

parser = argparse.ArgumentParser(
    description="AI Agent course from boot.dev"
)

parser.add_argument('prompt', type=str, help='Prompt to sent to AI')
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

args = parser.parse_args()
user_prompt = args.prompt
verbose = args.verbose

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a file specified in the file path or filename within the same folder",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path or filename including extension",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs or executes a python file specified in the file path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path or filename of the python file to execute or run",
            ),
        },
        required=["file_path"],
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Given a file path including the file name with extension, it creates a new text file or overrides an existin one with the provided content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path or filename of the file. The file could exist or not",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content of the file to write to",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

allowed_functions = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file
}

def call_function(function_call_part, verbose):
    function_name = function_call_part.name
    arguments = function_call_part.args.copy()
    arguments["working_directory"] = "calculator"

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    if not function_name in allowed_functions:
        return types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
        )

    function_to_call = allowed_functions[function_name]
    function_result = function_to_call(**arguments)

    return types.Part.from_function_response(
        name=function_name,
        response={"result": function_result},
    )

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

iteration_number = 0

while iteration_number < 20:
    iteration_number += 1

    response = client.models.generate_content(
        model = 'gemini-2.0-flash-lite',
        contents = messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt
        )
    )

    if not response.candidates:
        print(response.text)
        break

    if response.candidates[0].content:
        messages.append(response.candidates[0].content)
        for part in response.candidates[0].content.parts:
            if part.text:
                print(part.text)

    if response.function_calls != None and len(response.function_calls) > 0:
        types_parts = []
        for function_call_part in response.function_calls:
            types_part_result = call_function(function_call_part, verbose)
            types_parts.append(types_part_result)
            function_response = types_part_result.function_response.response
        messages.append(
            types.Content(
                role="tool",
                parts=types_parts
            )
        )
    else:
        print(response.text)
        break



if(verbose):
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")