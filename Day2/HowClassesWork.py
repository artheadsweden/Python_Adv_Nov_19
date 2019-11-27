class A:
    pass


class B:
    pass


class MyClass1(A, B):
    name = "MyClass 1"

    def message(self):
        return "I am " + self.name

# ======================================

def message(self):
    return "I am " + self.name


body = {'name': 'MyClass 2', 'message': message}

MyClass2 = type('MyClass2', (A, B), body)

# ======================================


def main():
    obj1 = MyClass1()
    print(obj1.message())
    obj2 = MyClass2()
    print(obj2.message())


if __name__ == '__main__':
    main()
