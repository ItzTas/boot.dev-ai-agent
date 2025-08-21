import os
from pathlib import Path
import subprocess
import sys

from functions.utils import is_outside_working_directory


def run_python_file(
    working_directory: str,
    file_path: str,
    args: list[str] = [],
) -> str:
    full_path = os.path.abspath(
        os.path.join(working_directory, file_path),
    )
    if is_outside_working_directory(working_directory, full_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not Path(full_path).exists():
        return f'Error: File "{file_path}" not found.'
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    args.insert(0, sys.executable)
    args.insert(1, file_path)
    output = None
    try:
        output = subprocess.run(
            args,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=os.path.abspath(working_directory),
        )
    except Exception as err:
        return f"Error: executing Python file: {err}"
    return _format_str_run_python_file(output)


def _format_str_run_python_file(output: subprocess.CompletedProcess[str]) -> str:
    stroutput = ""
    if output.stdout != "":
        stroutput += f"STDOUT: \n{output.stdout}\n"
    if output.stderr != "":
        stroutput += f"STDERR: \n{output.stderr}\n"
    if stroutput == "":
        stroutput += "No output produced.\n"
    if output.returncode != 0:
        stroutput += f"Process exited with code {output.returncode}\n"
    return stroutput
