import argparse
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.constants import MODEL


def main():
    _ = load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) == 1:
        print("must provide an argument")
        exit(1)

    user_prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model=MODEL,
        contents=messages,
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def add_flags() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    _ = parser.add_argument(
        '--verbose',
        action='store_true',
        help='Activates verbose logging'
    )
    return parser

def is_flag_active(flag: str, parser: argparse.ArgumentParser | None = None) -> bool:
    if parser is None:
        parser = add_flags()
    args = parser.parse_args(sys.argv[1:])
    return bool(getattr(args, flag, False))

def print_non_verbose(user_prompt: str):

def print_verbose():


if __name__ == "__main__":
    main()
