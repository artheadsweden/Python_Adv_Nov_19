class Meta(type):
    def __new__(cls, classname, bases, cls_dict):
        for name in cls_dict:
            if name != name.lower():
                raise TypeError("Please follow PEP8 naming convention")
        return super().__new__(cls, classname, bases, cls_dict)


class Root(metaclass=Meta):
    pass


class Level1(Root):
    pass


class Level2(Level1):
    def my_method(self):
        pass


def main():
    level2 = Level2()


if __name__ == '__main__':
    main()
