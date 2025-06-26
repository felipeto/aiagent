from google import genai
from google.genai import types

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    args = function_call_part.copy()
    args["working_directory"] = "calculator"

    return types.FunctionCall({'name' : function_call_part.name, 'args' : args})