
def function_object(n):
    private_value = n

    def func():
        print(f"{private_value=}")

    def increase_by(x):
        nonlocal private_value
        private_value += x

    def decrease_by(x):
        nonlocal private_value
        private_value -= x

    def get_value():
        return private_value

    def set_value(new_value):
        nonlocal private_value
        private_value = new_value

    func.increase_by = increase_by
    func.decrease_by = decrease_by
    func.get_value = get_value
    func.set_value = set_value

    return func


def main():
    fo1 = function_object(10)
    fo2 = function_object(100)

    print(fo1.get_value())
    print(fo2.get_value())
    fo1.increase_by(10)
    fo2.increase_by(10)
    print(fo1.get_value())
    print(fo2.get_value())


if __name__ == '__main__':
    main()
