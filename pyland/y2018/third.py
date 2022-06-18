
def find_similiar(number: str):
    mval = 10000000000000
    marr = []
    # if len == 2
    number = list(number.split(" "))
    for index in range(len(number) - 1):
        if type(number[index]) == str:
            number[index] = int(number[index])

        if type(number[index + 1]) == str:
            number[index + 1] = int(number[index+ 1])

        if number[index + 1] - number[index] < mval:
            mval = number[index + 1] - number[index]
            marr = [index]

        elif number[index + 1] - number[index] == mval:
            marr.append(index)

    mval = 1000000000000000000
    mind = 0

    for index in marr:
        temp = number[index] ^ number[index + 1]
        if temp < mval:
            mind = index
            mval = temp

    print(mval)
    print(mind)


if __name__ == '__main__':
    # no_of_test = int(input())
    #
    # for i in range(no_of_test):
    #     _ = input()
    #     number = input()
    find_similiar(input())