
def list_range(n):
    value = 0
    result_list = []
    while value < n:
        result_list.append(value)
        value += 1
    return result_list


def gen_range(n):
    value = 0
    while value < n:
        yield value
        value += 1


def main():
    for i in list_range(10):
        print(i)

    for i in gen_range(10):
        print(i)


if __name__ == '__main__':
    main()
