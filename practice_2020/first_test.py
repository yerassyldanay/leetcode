import math, time
from random import seed
from random import randint, random

from practice_2020.code import first

if __name__ == "__main__":
    ranges = []

    n = 10 #int(math.pow(10, 2))
    start, endwith = 1, int(math.pow(10, 6))
    for i in range(n):
        pivot = randint(start, endwith)
        delta = randint(0, 15)
        ranges.append((pivot, delta))

    remember_index = dict()
    for i, each in enumerate(ranges):
        remember_index[each] = i

    # range
    ranges_2 = ranges.copy()

    # global timer
    gstart = time.time()

    # sort
    start = time.time()
    ranges = sorted(ranges, key=lambda x: x[0])
    ranges_2 = sorted(ranges_2, key=lambda x: x[0])
    print("sort: ", time.time() - start)

    print(ranges)
    print("ranges")

    # faster
    start = time.time()
    s = first.AFirst()
    s.solve(ranges)
    print("faster: ", time.time() - start)

    print("it took: ", time.time() - gstart)

    # slower
    start = time.time()
    s = first.AFirstSolution()
    s.solve(ranges_2, remember_index)
    print("slower: ", time.time() - start)
