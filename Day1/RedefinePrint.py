from functools import wraps


def print_with_start(original_print):
    @wraps(original_print)
    def wrapper(*args, **kwargs):
        pre = ""
        if "start" in kwargs:
            pre = kwargs["start"]
            kwargs.pop("start")
        original_print(pre, *args, **kwargs)
    return wrapper


print = print_with_start(print)


def main():
    x = 10
    print("hi", x, sep="-", end="->\n", start="<-")
    print("Hi there", x)



if __name__ == '__main__':
    main()
