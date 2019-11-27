def funcfact(e):
    def wrapper(b):
        return b**e
    return wrapper


def main():
    square = funcfact(2)
    cube = funcfact(3)

    print(square(3))
    print(cube(3))

    ff = lambda e: lambda b: b**e
    sq = ff(2)
    cu = ff(3)
    print(sq(3))
    print(cu(3))


if __name__ == '__main__':
    main()
