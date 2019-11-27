def gen():

    for i in [1, 2, 3, 4, 5]:
        yield i**2

def main():
    for i in gen():
        print(i)


    for i in (i**2 for i in [1, 2, 3, 4, 5]):
        print(i)


if __name__ == '__main__':
    main()
