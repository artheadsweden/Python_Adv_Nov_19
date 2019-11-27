def ff(n):
    if n == 1:
        return 1
    return n * ff(n-1)

def main():

    bases = [2, 4, 8]
    result = sum(map(ff, bases))

    a = lambda s: sum(map(f:=lambda n: 1 if n == 1 else n * (f(n-1)), s))
    print(a(bases))

if __name__ == '__main__':
    main()
