from .number_list import NumberList


def nc_main() -> None:
    base, val = 36, "10"
    num_list = NumberList(base, val)
    print(f"{val}#{base} = {num_list.base10()}#10")
