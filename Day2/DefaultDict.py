from collections import defaultdict


def main():
    numbers = [1, 2, 1, 4, 2, 6, 6, 2, 4, 2]
    count = {}
    for value in numbers:
        if value not in count:
            count[value] = 1
            continue
        count[value] += 1

    print(count)

    count2 = defaultdict(int)
    for value in numbers:
        count2[value] += 1

    print(count2)


if __name__ == '__main__':
    main()
