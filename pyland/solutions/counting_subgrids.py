from typing import List

class Solution:

    def print(self, y, y2, x, x2):
        for ty in range(len(self.matrix)):
            for tx in range(len(self.matrix[0])):
                if (ty == y or ty == y2) and (tx == x or tx == x2):
                    print(" X ", end="")
                else:
                    if self.matrix[ty][tx]:
                        print(" 1 ", end="")
                    else:
                        print(" 0 ", end="")
            print()
        print()

    def find(self, matrix: List[List[int]]):
        self.matrix = matrix

        count = 0

        ylen = len(matrix)
        xlen = len(matrix[0])

        for y in range(0, ylen):
            for x in range(0, xlen):

                if matrix[y][x]:
                    for x2 in range(x+1, xlen):
                        if matrix[y][x2]:

                            for y2 in range(y + 1, ylen):
                                if matrix[y2][x] and matrix[y2][x2]:
                                    self.print(y, y2, x, x2)
                                    count += 1

        return count

matrix = [[0, 1, 0, 0, 1], [0, 1, 1, 0, 0], [1, 0, 0, 0, 0], [0, 1, 1, 0, 1]]

# s = Solution()
# a = s.find(matrix)
# print(a)


a = [2, 2, 18, 12, 1, 22, 0]

def counter(x: int):

    return counter

for f in range(len(a)):
    for s in range(f + 1, len(a)):
        union = a[f] & a[s]

        if union and counter(union) >= 1:
            print(a[f], " & ", a[s], " = ", a[f] & a[s])


print()

print(counter(64))
