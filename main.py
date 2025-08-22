import os
import sys
from dotenv import load_dotenv
from google import genai
from classes.client import Client
from classes.function_call_processor import FunctionCallProcessor
from functions.flags import get_arg_parser, get_flags, is_flag_active
from functions.print import print_function_calls, print_non_verbose, print_verbose


def main():
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()
    flags = get_flags()

    _ = load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) == 1:
        print("must provide an argument")
        exit(1)

    user_prompt = args.prompt

    client = Client()
    response = client.generate_first_content(user_prompt)

    working_directory = "calculator"
    processor = FunctionCallProcessor(working_directory)
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
