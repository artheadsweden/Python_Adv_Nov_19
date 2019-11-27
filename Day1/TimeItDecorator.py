import time
from functools import wraps


def time_it(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        stop = time.time()
        print(f"Call to {f.__name__} took {stop-start} seconds")
        return result
    return wrapper


@time_it
def time_me(s):
    print("Going to sleep")
    time.sleep(s)
    print("I'm back")


def main():
    time_me(3)


if __name__ == '__main__':
    main()
