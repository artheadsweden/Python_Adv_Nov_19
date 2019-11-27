from functools import wraps


def add_chars(pre_str, post_str):
    def decorate(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return pre_str + f(*args, **kwargs) + post_str
        return wrapper
    return decorate


@add_chars("-= ", " =-")
def gen_message(greeting, name):
    return f"{greeting}, {name}!"


def main():
    print(gen_message("Yo", "Bob"))


if __name__ == '__main__':
    main()
