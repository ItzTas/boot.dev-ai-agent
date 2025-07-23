import argparse
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.constants import MODEL, VERBOSE_FLAG


def main():
    arg_parser = add_flags()
    args = arg_parser.parse_args()

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
    )

    if is_flag_active(VERBOSE_FLAG["name"], arg_parser):
        print_verbose(
            user_prompt,
            response,
        )
    else:
        print_non_verbose(user_prompt, response)


def add_flags() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    _ = parser.add_argument(
        "prompt",
        type=str,
        help="User prompt text",
    )

    _ = parser.add_argument(
        f"--{VERBOSE_FLAG['name']}",
        action=VERBOSE_FLAG["action"],
        help=VERBOSE_FLAG["description"],
    )
    return parser


def is_flag_active(flag: str, parser: argparse.ArgumentParser | None = None) -> bool:
    if parser is None:
        parser = add_flags()
    args = parser.parse_args(sys.argv[1:])
    return bool(getattr(args, flag, False))


def print_non_verbose(user_prompt: str, response: types.GenerateContentResponse):
    print(user_prompt)
    print(response.text)


def print_verbose(user_prompt: str, response: types.GenerateContentResponse):
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
