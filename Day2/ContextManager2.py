from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    # Consider this to be the __enter__
    print("Opening the file", filename)
    the_file = open(filename, mode)
    yield the_file

    # Consider this to be __exit__
    print("Closing file")
    the_file.close()

def main():
    with open_file("text3.txt", "w") as file:
        file.write("Hi\n")
        file.write("Bye\n")
    print("All done")


if __name__ == '__main__':
    main()
