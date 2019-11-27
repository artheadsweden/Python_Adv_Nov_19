from pympler import asizeof


class NoSlots:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

class WithSlots:
    __slots__ = ["name", "identifier"]

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


def main():
    no_slots = [NoSlots(str(n), n) for n in range(100_000)]
    no_slot_size = round(asizeof.asizeof(no_slots)/1024/1024, 2)

    print("NoSlots =", no_slot_size, "mb")

    with_slots = [WithSlots(str(n), n) for n in range(100_000)]
    with_slot_size = round(asizeof.asizeof(with_slots)/1024/1024, 2)

    print("WithSlots =", with_slot_size, "mb")

if __name__ == '__main__':
    main()
