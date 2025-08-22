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
    messages: list[types.Content]

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
        self.messages = []

    def generate_first_content(
        self,
        user_prompt: str | None = None,
    ) -> types.GenerateContentResponse:
        if user_prompt is None:
            args = self.arg_parser.parse_args()
            user_prompt = args.prompt

        self.messages.append(
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
        )
        response = self.client.models.generate_content(
            model=MODEL,
            contents=self.messages,
            config=types.GenerateContentConfig(
                tools=[get_available_functions()],
                system_instruction=SYSTEM_PROMPT,
            ),
        )
        if response.candidates and response.candidates[0].content:
            self.messages.append(response.candidates[0].content)

        return response

    def generate_content(
        self,
        new_messages: list[types.Content],
    ) -> types.GenerateContentResponse:
        self.messages.extend(new_messages)
        response = self.client.models.generate_content(
            model=MODEL,
            contents=self.messages,
            config=types.GenerateContentConfig(
                tools=[get_available_functions()],
                system_instruction=SYSTEM_PROMPT,
            ),
        )
        if response.candidates and response.candidates[0].content:
            self.messages.append(response.candidates[0].content)
        return response
