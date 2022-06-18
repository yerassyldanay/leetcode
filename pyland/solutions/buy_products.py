from typing import List

class Solution:
    def buy(self, matrix: List[List[int]]):

        plen = len(matrix)
        dlen = len(matrix[0])

        stack = []
        bought = set()

        def help(day: int, cost: int):
            # bought all products
            if plen == len(stack):
                print(stack)
                return cost

            # no time left
            if day == dlen:
                return float("inf")

            # try to buy all products  on this day
            costArr = [float("inf")]
            for i in range(plen):
                if i not in bought:
                    stack.append((i, day))
                    bought.add(i)
                    costArr.append(help(day + 1, cost + matrix[i][day]))
                    bought.pop()
                    stack.pop()

            costNothing = help(day + 1, cost)

            return min(min(costArr), costNothing)

        return help(0, 0)

# matrix = [[6, 9, 5, 2, 8, 9, 1, 6], [8, 2, 6, 2, 7, 5, 7, 2], [5, 3, 9, 7, 3, 5, 1, 4]]
#
# s = Solution()
# a = s.buy(matrix, )
#
# print(a)

n = 5
sumof = [1] * (1 << n)
_nbit = 1 << n

print(_nbit)

for _num in range(n):
    for _set in range(0, _nbit):

        print(_set, "&", (1 << _num), _set & (1 << _num))
        print(_set, "^", (1 << _num), _set ^ (1 << _num))
        print()

        if _num & _set:
            sumof[_set] += sumof[_set ^ (1 << _num)]

print(list(range(1 << n)))
print(sumof)