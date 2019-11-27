def func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

def main():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8)

    first, *_, second_last, last = numbers
    print(first, second_last, last)


if __name__ == '__main__':
    main()
