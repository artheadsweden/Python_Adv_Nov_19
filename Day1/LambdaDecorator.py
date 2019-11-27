gen_chars = lambda f: lambda *args, **kwargs: "<<< " + f(*args, **kwargs) + " >>>"


@gen_chars
def gen_message(greeting, name):
    return f"{greeting}, {name}!"


def main():
    print(gen_message("Hi", "Sara"))


if __name__ == '__main__':
    main()
