from .number_list import NumberList


def nc_main() -> None:
    base, val = 16, "A"
    nl = NumberList(base, val)
    print(f"{val}#{base} = {nl.base10()}#10 = {nl.change_base(2).num}#2")
