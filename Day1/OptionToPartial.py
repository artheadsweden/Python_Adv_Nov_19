def power(base, exp):
    return base**exp


def power_factory(f, ex):
    def inner(b):
        return f(b, ex)
    return inner


def main():
    square = power_factory(power, 2)
    cube = power_factory(power, 3)

    print(square(3))
    print(cube(3))

if __name__ == '__main__':
    main()
