def main():
    data = "0989078298729387298730982987987123897987239871928732987298379827398"
    price = data[13:16]
    amount = data[21:23]
    print(price, amount)

    PRICE = slice(13, 16)
    AMOUNT = slice(21, 23)

    price = data[PRICE]
    amount = data[AMOUNT]
    print(price, amount)


if __name__ == '__main__':
    main()
