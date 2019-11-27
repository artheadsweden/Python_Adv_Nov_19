from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str

    def birthday(self):
        self.age += 1


def main():
    p1 = Person("Bob", 34, "bob@email.com")
    p2 = Person("Anna", 23, "anna@mail.com")
    print(p1)
    print(p2)
    p2.birthday()
    print(p2)


if __name__ == '__main__':
    main()
