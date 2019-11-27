from collections import defaultdict


def main():
    ice_cream = defaultdict(lambda: 'Vanilla')
    ice_cream['Alice'] = 'Chunky Bits'
    ice_cream['Bob'] = 'Good Butter'

    print(ice_cream['Alice'])
    print(ice_cream['Bob'])
    print(ice_cream['John'])


if __name__ == '__main__':
    main()
