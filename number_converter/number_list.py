from .base36 import BASE36_TO_BASE10_MAP


def trim_non_base36_symbols(txt: str) -> str:
    """
    Remove any symbols from `txt` that don't fit in base-36 and return the
    cleaned string.
    """
    allowed = BASE36_TO_BASE10_MAP.keys()
    valid_string: str = ""
    for char in txt.upper():
        if char in allowed:
            valid_string += char
    return valid_string


class NumberList:
    def __init__(self, base: int, nums: str) -> None:
        self.base: int = base
        self.num: str = trim_non_base36_symbols(nums)

    def base10(self) -> int:
        """Convert the number in `self.num` to a base-10 `int`."""
        worth: int = len(self.num) - 1
        result: int = 0
        for c in self.num:
            result += BASE36_TO_BASE10_MAP[c] * self.base ** worth
            worth -= 1
        return result
