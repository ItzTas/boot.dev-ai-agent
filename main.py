import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from constants import MODEL, SYSTEM_PROMPT
from functions.flags import add_flags, get_flags, is_flag_active
from functions.functions import get_available_functions
from functions.print import print_function_calls, print_non_verbose, print_verbose


def main():
    arg_parser = add_flags()
    args = arg_parser.parse_args()
    flags = get_flags()
    available_functions = get_available_functions()

    _ = load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) == 1:
        print("must provide an argument")
        exit(1)

    user_prompt = args.prompt

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model=MODEL,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=SYSTEM_PROMPT,
        ),
    )

    if response.function_calls:
        print_function_calls(response.function_calls)

    if is_flag_active(flags["verbose"]["name"], arg_parser):
        print_verbose(
            user_prompt,
            response,
        )
    else:
        print_non_verbose(user_prompt, response)


if __name__ == "__main__":
    main()
