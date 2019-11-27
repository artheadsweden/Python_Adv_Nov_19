class MyMeta(type):
    def __init__(cls, name, bases, dct):
        print(f"{name=}")
        print(f"{bases=}")
        print(f"{dct=}")
        super(MyMeta, cls).__init__(name, bases, dct)


class MyClass(metaclass=MyMeta):
    pass

def main():
    obj = MyClass()


if __name__ == '__main__':
    main()
