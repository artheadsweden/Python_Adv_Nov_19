from collections import namedtuple


def main():
    Student = namedtuple('Student', ['name', 'age', 'email'])
    s = Student("John", email="john@email.com", age=15)

    print(s.name)
    print(s.age)
    print(s[2])


if __name__ == '__main__':
    main()
