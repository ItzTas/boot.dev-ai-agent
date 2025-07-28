import os
from functions.utils import is_outside_working_directory, read_file


def get_file_content(working_directory: str, file_path: str):
    full_path = os.path.abspath(
        os.path.join(working_directory, file_path),
    )
    if is_outside_working_directory(working_directory, full_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        return read_file(full_path)
    except (FileNotFoundError, PermissionError) as e:
        return f"Error: {e}"
