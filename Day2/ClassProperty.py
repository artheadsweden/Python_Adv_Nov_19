class P:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

def main():
    p1 = P(500)
    print(p1.x)
    p2 = P(2000)
    print(p2.x)
    p2.x = 10000
    print(p2.x)



if __name__ == '__main__':
    main()
