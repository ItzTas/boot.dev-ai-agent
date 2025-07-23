from typing import TypedDict


class FlagSpec(TypedDict):
    name: str
    type: type
    action: str
    description: str


VERBOSE_FLAG: FlagSpec = {
    "name": "verbose",
    "type": bool,
    "action": "store_true",
    "description": "Activates verbose logging",
}

MODEL = "gemini-2.0-flash-001"
