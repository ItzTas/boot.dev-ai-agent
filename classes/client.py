from argparse import ArgumentParser
import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

from constants import MODEL, SYSTEM_PROMPT
from functions.flags import get_arg_parser
from functions.functions import get_available_functions


class Client:
    client: genai.Client
    model: str
    arg_parser: ArgumentParser
    system_prompt: str

    def __init__(
        self,
        arg_parser: ArgumentParser | None = None,
        model: str = MODEL,
        system_prompt: str = SYSTEM_PROMPT,
    ) -> None:
        if arg_parser is None:
            self.arg_parser = get_arg_parser()

        _ = load_dotenv()
        api_key = os.environ.get("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

        self.model = model
        self.system_prompt = system_prompt

    def generate_first_content(
        self,
        user_prompt: str | None = None,
    ) -> types.GenerateContentResponse:
        if user_prompt is None:
            args = self.arg_parser.parse_args()
            user_prompt = args.prompt

        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        response = self.client.models.generate_content(
            model=MODEL,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[get_available_functions()],
                system_instruction=SYSTEM_PROMPT,
            ),
        )
        return response
