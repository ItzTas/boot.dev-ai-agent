import argparse
import sys
from functions.types import FlagSpec, Flags


def get_flags() -> Flags:
    verbose: FlagSpec = {
        "name": "verbose",
        "type": bool,
        "action": "store_true",
        "description": "Activates verbose logging",
    }

    flags: Flags = {
        "verbose": verbose,
    }
    return flags


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    _ = parser.add_argument(
        "prompt",
        type=str,
        help="User prompt",
    )

    flags = get_flags()
    for flag_name in flags.keys():
        flag_spec = flags[flag_name]
        if not any(flag_name in action.option_strings for action in parser._actions):
            _ = parser.add_argument(
                f"--{flag_spec['name']}",
                action=flag_spec["action"],
                help=flag_spec["description"],
            )

    return parser


def is_flag_active(flag: str, parser: argparse.ArgumentParser | None = None) -> bool:
    if parser is None:
        parser = get_arg_parser()
    args = parser.parse_args(sys.argv[1:])
    return bool(getattr(args, flag, False))
