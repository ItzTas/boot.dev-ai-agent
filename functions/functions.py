from typing import cast
from google.genai import types

from functions.types import Schemas


def get_available_functions() -> types.Tool:
    function_schemas: list[types.FunctionDeclaration] = [
        cast(types.FunctionDeclaration, val) for val in get_function_schemas().values()
    ]
    return types.Tool(
        function_declarations=function_schemas,
    )


def get_function_schemas() -> Schemas:
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="List files in the especified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    schemas: Schemas = {
        "get_files_info": schema_get_files_info,
    }
    return schemas
