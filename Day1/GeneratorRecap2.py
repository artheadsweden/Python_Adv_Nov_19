def gen_range(n):
    print("Starting generator")
    value = 0
    while value < n:
        yield value
        value += 1


def main():
    g = gen_range(3)
    print(type(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))



if __name__ == '__main__':
    main()
