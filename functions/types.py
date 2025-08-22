from typing import Any, Callable, TypedDict

from google.genai import types


class FlagSpec(TypedDict):
    name: str
    type: type
    action: str
    description: str


class Flags(TypedDict):
    verbose: FlagSpec


class FunctionSchema:
    function_declaration: types.FunctionDeclaration
    fn: Callable[..., str]

    def __init__(
        self,
        function_declaration: types.FunctionDeclaration,
        fn: Callable[..., Any],
    ) -> None:
        self.function_declaration = function_declaration
        self.fn = fn


class Schemas(TypedDict):
    get_files_info: FunctionSchema
