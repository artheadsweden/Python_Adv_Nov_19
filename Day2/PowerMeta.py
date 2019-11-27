from functools import partial

def power(base, exp):
    return base**exp

class PowerMeta(type):
    def __init__(cls, name, bases, dct):
        for x in range(1, 51):
            setattr(cls, f"p{x}", partial(power, exp=x))
        super(PowerMeta, cls).__init__(name, bases, dct)

class Power(metaclass=PowerMeta):
    pass

def main():
    p = Power()
    print(p.p3(3))
    print(p.p4(3))
    print(p.p45(3))


if __name__ == '__main__':
    main()
