class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = value

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32

def main():
    c1 = Celsius(-500)
    print(c1.temperature)
    c1.temperature = 37
    print(c1.temperature)
    print(c1.to_farenheit())


if __name__ == '__main__':
    main()
