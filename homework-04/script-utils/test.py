
def prova(num:int):
    rest = num % 4
    test = num & 3
    if rest != test:
        print("num {}".format(num))


if __name__ == '__main__':
    for i in range(pow(2,32) - 1):
        prova(i)
