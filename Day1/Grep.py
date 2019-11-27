def grep(pattern, case=True):
    print(f"Search for pattern {pattern}")
    pattern = pattern if case else pattern.lower()
    while True:
        line = yield
        line = line if case else line.lower()
        if pattern in line:
            print(f"Found {pattern} in line {line.strip()}")


def main():
    search = grep("hello", False)
    next(search)
    with open("input.txt", "r") as infile:
        for line in infile:
            search.send(line)



if __name__ == '__main__':
    main()
