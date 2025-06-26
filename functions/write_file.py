import os

def write_file(working_directory, file_path, content):
    path_working_directory = os.path.abspath(working_directory)
    if not file_path.startswith("/"):
        path_file_path = os.path.abspath(working_directory + "/" + file_path)
    else:
        path_file_path = os.path.abspath(file_path)

    if not path_file_path.startswith(path_working_directory):
        raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        
    target_folder = f"{working_directory}/{file_path}"
    if working_directory in os.path.abspath(target_folder):
        if not(os.path.exists):
            os.makedirs(target_folder)
        return _write_file_content(target_folder, content)

def _write_file_content(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'