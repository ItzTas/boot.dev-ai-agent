import argparse
import sys

from flags.types import FlagSpec


def get_flags() -> dict[str, FlagSpec]:
    verbose: FlagSpec = {
        "name": "verbose",
        "type": bool,
        "action": "store_true",
        "description": "Activates verbose logging",
    }

    flags = {"verbose": verbose}
    return flags


def add_flags() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    _ = parser.add_argument(
        "prompt",
        type=str,
        help="User prompt text",
    )

    verbose_flag = get_flags()["verbose"]

    _ = parser.add_argument(
        f"--{verbose_flag['name']}",
        action=verbose_flag["action"],
        help=verbose_flag["description"],
    )
    return parser


def is_flag_active(flag: str, parser: argparse.ArgumentParser | None = None) -> bool:
    if parser is None:
        parser = add_flags()
    args = parser.parse_args(sys.argv[1:])
    return bool(getattr(args, flag, False))
