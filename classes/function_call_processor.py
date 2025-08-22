from google.genai.types import FunctionCall

from functions.functions import get_function_schema_by_name
from functions.print import print_function_call


class FunctionCallProcessor:
    working_directory: str

    def __init__(self, working_directory: str) -> None:
        self.working_directory = working_directory

    def process_function_call(self, function_call: FunctionCall):
        name = function_call.name
        if not name:
            return
        schema = get_function_schema_by_name(name)
        if not schema:
            print(f"Schema with name: {name} does not exist")
            exit(1)

        fn = schema.fn
        call_args = function_call.args.copy()
        call_args["working_directory"] = self.working_directory

        print_function_call(function_call)

        _ = fn(**call_args)

    def process_function_calls(self, function_calls: list[FunctionCall]):
        for function_call in function_calls:
            self.process_function_call(function_call)
