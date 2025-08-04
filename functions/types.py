from typing import TypedDict


class FlagSpec(TypedDict):
    name: str
    type: type
    action: str
    description: str
