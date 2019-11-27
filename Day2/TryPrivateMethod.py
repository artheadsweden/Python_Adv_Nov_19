from Private import private


class MyClass:
    def first(self):
        self.second()
        print("First")

    @private
    def second(self):
        print("Second")

def main():
    mc = MyClass()
    mc.first()
    #mc.second()


if __name__ == '__main__':
    main()
