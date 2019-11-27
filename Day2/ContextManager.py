class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file", self.filename)
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file")
        self.open_file.close()


def main():
    with File("text2.txt", "w") as file:
        file.write("Hi\n")
        file.write("Bye\n")
    print("All done")

if __name__ == '__main__':
    main()
