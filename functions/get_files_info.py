import os


def is_outside_working_directory(working_directory: str, full_path: str) -> bool:
    abs_work_dir = os.path.abspath(working_directory)
    return not full_path.startswith(abs_work_dir)


def get_files_info(working_directory: str, directory: str = ".") -> str:
    full_path = os.path.abspath(
        os.path.join(working_directory, directory),
    )
    if is_outside_working_directory(working_directory, full_path):
        return f'   Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'   Error: "{directory}" is not a directory'
    return format_dir_contents(full_path)


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
