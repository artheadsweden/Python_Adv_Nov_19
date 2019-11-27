from collections import Counter


def main():
    numbers = [1, 2, 1, 4, 2, 6, 6, 2, 4, 2]
    count = Counter(numbers)
    print(count)

    text = "When I was a kid I always wanted a cat but all I got was a gold fish"
    word_count = Counter(text.split())
    for w, c in word_count.most_common(3):
        print(w, "=>", c)


if __name__ == '__main__':
    main()
