import os
import subprocess

def run_python_file(working_directory, file_path):
    path_working_directory = os.path.abspath(working_directory)
    if not file_path.startswith("/"):
        path_file_path = os.path.abspath(working_directory + "/" + file_path)
    else:
        path_file_path = os.path.abspath(file_path)

    if not path_file_path.startswith(path_working_directory):
        raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.exists(file_path):
        raise Exception(f'Error: File "{file_path}" not found.')
    
    if not file_path.endswith(".py"):
        raise Exception(f'Error: "{file_path}" is not a Python file.')
    
    try:
        result = subprocess.run('python3 ' + path_file_path, timeout=30, capture_output=True, text=True, check=True, shell=True)
        output_parts = []

        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout.strip()}")

        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr.strip()}")

        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not output_parts:
            return "No output produced."
        
        return output_parts
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
