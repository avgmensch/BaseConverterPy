from sys import argv as args
from .number_list import NumberList


def number_converter_cli() -> None:
    argstr: str = "".join(args)

    if len(args) == 1 or len(args) > 3 or "-h" in argstr or "--help" in argstr:
        print(
            "Convert a number from one base to another.\n"
            f"Usage: {args[0]} <number>/<old-base> <new-base>\n"
            "\n"
            "Examples:\n"
            f"{args[0]} FF/16 2    Output: 11111111\n"
            f"{args[0]} 1010/2 10  Output: 10\n"
            "\n"
            "Options:\n"
            "-h, --help    Show this message"
        )

    num, old_base = args[1].split("/")
    new_base = args[2]

    nl = NumberList(int(old_base), num)
    print(nl.change_base(int(new_base)).num)
