from google.genai import types
from google.genai.types import FunctionCall

from functions.functions import get_function_schema_by_name
from functions.print import print_function_call


class FunctionCallProcessor:
    working_directory: str

    def __init__(self, working_directory: str) -> None:
        self.working_directory = working_directory

    def process_function_call(self, function_call: FunctionCall) -> types.Part | None:
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

        output = fn(**call_args)
        function_response_dict = {
            "output": output,
            "function_name": name,
        }
        return types.Part(
            function_response=types.FunctionResponse(
                name=name,
                response=function_response_dict,
            ),
        )

    def process_function_calls(
        self, function_calls: list[FunctionCall]
    ) -> types.Content:
        parts: list[types.Part] = []
        for function_call in function_calls:
            result = self.process_function_call(function_call)
            if not result:
                continue
            parts.append(result)
        return types.Content(role="tool", parts=parts)
