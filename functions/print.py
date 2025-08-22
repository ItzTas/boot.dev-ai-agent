from google.genai import types


def print_non_verbose(
    user_prompt: str,
    response: types.GenerateContentResponse,
) -> None:
    print(user_prompt)
    print(response.text)


def print_verbose(user_prompt: str, response: types.GenerateContentResponse) -> None:
    print(response.text)
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


def print_function_calls(function_calls: list[types.FunctionCall]) -> None:
    if not function_calls:
        return
    for function_call in function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
