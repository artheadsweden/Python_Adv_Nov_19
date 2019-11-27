
def add_chars(f):
    def wrapper(*args, **kwargs):
        return "<<< " + f(*args, **kwargs) + " >>>"
    return wrapper

@add_chars
def gen_message(greeting, name):
    return f"{greeting}, {name}!"


def main():
    #global gen_message
    #gen_message = add_chars(gen_message)
    print(gen_message("Hi", "Anna"))


if __name__ == '__main__':
    main()
