import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    if working_directory.startswith('/'):
        working_directory = working_directory[1:]
        
    target_file = f"{working_directory}/{file_path}"
    target_file_abs_path = os.path.abspath(target_file)
    target_file_abs_path_contents = target_file_abs_path.split("/")
    target_file_folder = None
    if len(target_file_abs_path_contents) > 1:
        target_file_folder = "/".join(target_file_abs_path_contents[0:len(target_file_abs_path_contents) - 2])
    if target_file_folder != None and os.path.isfile(target_file) and working_directory in os.path.abspath(target_file):
        return _file_content(target_file)
    
    raise Exception(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

def _file_content(target_file):
    file_content_str = '';
    with open(target_file, "r") as f:
        file_content_str = f.read(MAX_CHARS)

    if len(file_content_str) >= MAX_CHARS:
        file_content_str += '[...File "{target_file}" truncated at 10000 characters]'

    return file_content_str