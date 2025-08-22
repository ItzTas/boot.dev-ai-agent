from typing import cast
from google.genai import types

from functions.get_files_info import get_files_info
from functions.types import FunctionSchema, Schemas


def get_available_functions() -> types.Tool:
    function_schemas = get_function_declaration_list()
    return types.Tool(
        function_declarations=function_schemas,
    )


def get_function_declaration_list() -> list[types.FunctionDeclaration]:
    function_declarations: list[types.FunctionDeclaration] = []
    for val in get_function_schemas().values():
        val = cast(FunctionSchema, val)
        function_declarations.append(val.function_declaration)

    return function_declarations


def get_function_schema_by_name(name: str) -> FunctionSchema | None:
    schemas = get_function_schemas()
    schema = schemas.get(name)
    if not schema:
        return None
    return cast(FunctionSchema, schema)


def get_function_schemas() -> Schemas:
    schema_get_files_info = FunctionSchema(
        function_declaration=types.FunctionDeclaration(
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
        ),
        fn=get_files_info,
    )

    schemas: Schemas = {
        "get_files_info": schema_get_files_info,
    }
    return schemas
