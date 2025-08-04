import os
from functions.utils import is_outside_working_directory


def write_file(working_directory: str, file_path: str, content: str):
    full_path = os.path.abspath(
        os.path.join(working_directory, file_path),
    )
    if is_outside_working_directory(working_directory, full_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    dirname = os.path.dirname(full_path)
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except Exception as e:
            return f"Error: {e}"
    with open(full_path, "w") as f:
        try:
            _ = f.write(content)
        except Exception as e:
            return f"Error: {e}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
