from typing import TypedDict

from google.genai import types


class FlagSpec(TypedDict):
    name: str
    type: type
    action: str
    description: str


class Flags(TypedDict):
    verbose: FlagSpec


class Schemas(TypedDict):
    get_files_info: types.FunctionDeclaration
