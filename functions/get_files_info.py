import os

from functions.utils import format_dir_contents, is_outside_working_directory


def get_files_info(working_directory: str, directory: str = ".") -> str:
    full_path = os.path.abspath(
        os.path.join(working_directory, directory),
    )
    if is_outside_working_directory(working_directory, full_path):
        return f'   Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'   Error: "{directory}" is not a directory'
    return format_dir_contents(full_path)
