class A:
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})


def main():
    a = A(1, 2, 3, 4, 5, 6)
    print(a.a, a.b, a.c)


if __name__ == '__main__':
    main()
