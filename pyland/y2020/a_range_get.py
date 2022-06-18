import math
from random import seed
from random import randint, random
# seed random number generator
seed(2)

if __name__ == "__main__":
    ranges = [(1, 4), (4, 11), (8, 5), (12, 4)]

    range_find = []

    index = 0
    for i, each_range in enumerate(ranges):
        while index <= each_range[0]:
            range_find.append(i)
            index += 1

    print(list(range(len(range_find))))
    print(range_find)

    ranges = []

    n = int(math.pow(10, 5))
    start, endwith = 1, int(math.pow(10, 9))
    for i in range(n):
        pivot = randint(start, endwith)
        delta = randint(0, 15)
        ranges.append((pivot, delta))



    print(ranges)
    print(len(ranges))
