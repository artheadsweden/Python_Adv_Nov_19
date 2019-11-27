def gen_co():
    data = yield "Hello"
    yield data

def gen_co2():
    data = "Empty"
    while True:
        data += yield data


def gen_co3(data):
    while True:
        f = yield
        f(data)

def main():
    # gc = gen_co()
    # print(next(gc))
    # print(gc.send("World"))

    # gc = gen_co2()
    # print(next(gc))
    # print(gc.send("Oh"))
    # print(gc.send("OK"))
    # print(gc.send("Yes"))
    gc = gen_co3("Hi there")
    next(gc)
    gc.send(lambda value: print(value[::-1]))
    gc.send(lambda value: print(value))
    gc.send(print)




if __name__ == '__main__':
    main()
