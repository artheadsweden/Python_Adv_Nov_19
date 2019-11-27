def gen_range(n):
    print("Starting generator")
    value = 0
    while value < n:
        yield value
        value += 1


def main():
    for i in gen_range(100000):
        if i == 7:
            break
        print(i)


if __name__ == '__main__':
    main()
