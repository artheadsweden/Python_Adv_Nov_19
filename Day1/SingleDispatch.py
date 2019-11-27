from functools import singledispatch


@singledispatch
def func(arg, verbose=False):
    if verbose:
        print("Let me just say, ", end="")
    print(arg)


@func.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in the numbers, ", end="")
    print(arg)

@func.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, item in enumerate(arg):
        print(i, item)


def main():
    func(10, True)
    func("Hi", True)
    func([1, 2, 3], True)


if __name__ == '__main__':
    main()
