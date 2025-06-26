from functions import get_files_info, get_file_content, run_python_file, write_file
print("Available names:", [name for name in dir() if not name.startswith('_')])