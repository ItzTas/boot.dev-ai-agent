import os

from constants import FILE_READ_MAX_CHARS


def is_outside_working_directory(working_directory: str, full_path: str) -> bool:
    abs_work_dir = os.path.abspath(working_directory)
    return not full_path.startswith(abs_work_dir)


def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read(FILE_READ_MAX_CHARS)


def format_file_metadata(path: str, name: str) -> str:
    full_path = os.path.abspath(
        os.path.join(path, name),
    )
    size = -1
    is_dir = False
    try:
        size = os.path.getsize(full_path)
        is_dir = os.path.isdir(full_path)
    except OSError as err:
        return f"   Error: {err}"
    return f"   - {name}: file_size={size}, is_dir={is_dir}"


def format_dir_contents(path: str) -> str:
    names = os.listdir(path)
    formated_vals = ""
    for name in names:
        form = format_file_metadata(path, name)
        formated_vals += f"{form}\n"
    return formated_vals
