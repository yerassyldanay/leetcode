def solve(c):

    def help(a, coeff):
        if type(a) != list:
            return a

        summed = 0
        for each in a:
            if type(each) == list:
                summed += help(each, coeff + 1)
            else:
                summed += each

        return summed * coeff

    return help(c, 1)

assert solve([1, 2]) == 3
assert solve([1, 2, [3]]) == 9
assert solve([1, 2, [3, [4]], 5]) == 38

print(solve([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
