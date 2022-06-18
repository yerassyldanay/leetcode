import math
from collections import defaultdict

class Solution:
    def __increment(self, key: int, d: defaultdict):
        if key not in d:
            d[key] = 0

        d[key] += 1

    def __convert(self, num: int) -> defaultdict:
        t = num
        d = defaultdict()

        while True:
            entered = False
            for i in range(2, num):
                if num % i == 0:
                    self.__increment(i, d)
                    num //= i
                    entered = True

            if not entered and num != 1:
                self.__increment(num, d)

            if not entered:
                break

        # print(t, d)
        return d

    def nok(self, x, y: int):
        d1 = self.__convert(x)
        d2 = self.__convert(y)

        result = 1
        for key, value in d1.items():
            if key in d2:
                result *= int(math.pow( key, min(value, d2[key]) ))

        return result

    def ways(self, fv, sv):
        count = 0
        multiply = fv * sv
        for i in range(fv, multiply + 1):
            if i % fv == 0 and (multiply // i) % fv == 0 and multiply % i == 0:
                nok = s.nok(i, multiply // i)
                # print(i, nok)
                if nok == fv and sv == (multiply // nok):
                    # print(i, multiply // i)
                    count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    tests = [((5, 10), 2) , ((10, 11), 0), ((527, 9486), 4)]

    for test in tests[:]:
        fv, sv = test[0]
        count = test[1]

        tcount = s.ways(fv, sv)

        if tcount != count:
            print("expected ", count, " but got ", tcount)
        else:
            print(fv, sv, count, "ways")

