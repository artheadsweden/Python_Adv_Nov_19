from functools import partial


def power(base, exp):
    return base**exp


def main():
    result = power(3, 2)
    print(result)

    sqaure = partial(pow, exp=2)
    cube = partial(pow, exp=3)
    print(sqaure(3))
    print(cube(3))


if __name__ == '__main__':
    main()
