import math
from typing import List
from collections import defaultdict as dd

# ...... x = len(m[0])
# .
# y = len(m)
class Solution:

    def findMinimumPath(self, matrix: List[List[int]]):
        y = len(matrix)
        x = len(matrix[0])

        self.d = [[-1] * x for _ in range(y)]
        result = self.__dp(x - 1, y - 1, matrix)
        return result

    def __dp(self, x, y: int, matrix: List[List[int]]):

        if x == 0 and y == 0:
            return matrix[y][x]

        if len(matrix[0]) <= x or x < 0:
            return float("inf")

        if len(matrix) <= y or y < 0:
            return float("inf")

        if self.d[y][x] == -1:
            self.d[y][x] = min(self.__dp(x-1, y, matrix), self.__dp(x, y - 1, matrix)) + matrix[y][x]

        return self.d[y][x]

s = Solution()

matrix = [[3, 2, 1, 3], [1, 9, 2, 3], [9, 1, 5, 4]]
for each in matrix:
    print(each)

a = s.findMinimumPath(matrix)
print("min path: ", a)
