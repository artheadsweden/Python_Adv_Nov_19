import time
from functools import wraps
import requests


def cache(f):
    saved = {}
    @wraps(f)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in saved:
            return saved[key]
        result = f(*args, **kwargs)
        saved[key] = saved
        return result
    return wrapper


@cache
def web_lookup2(url):
    return requests.get(url).text


def web_lookup(url, cache={}):
    if url in cache:
        return cache[url]
    result = requests.get(url).text
    cache[url] = result
    return result


def main():
    url = "http://cnn.com"
    start = time.time()
    result = web_lookup2(url)
    end = time.time()
    print(f"It took {end-start} seconds")
    start = time.time()
    result = web_lookup2(url)
    end = time.time()
    print(f"It took {end-start} seconds")


if __name__ == '__main__':
    main()
