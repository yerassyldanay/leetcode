from typing import List

class Solution:
    def uniquePathsWithObstacles(self, matrix: List[List[int]]) -> int:
        for y, row in enumerate(matrix):
            for x, _ in enumerate(row):
                if y == 0 and x == 0:
                    matrix[y][x] = (matrix[y][x] + 1) % 2


                elif y == 0 and matrix[y][x] != 1:
                    matrix[y][x] = matrix[y][x - 1]

                elif x == 0 and matrix[y][x] != 1:
                    matrix[y][x] = matrix[y - 1][x]

                elif matrix[y][x] == 1:
                    matrix[y][x] = 0

                else:
                    matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]

        ylen = len(matrix)
        xlen = len(matrix[0])

        for row in matrix:
            print(row)

        return matrix[ylen - 1][xlen - 1]


if __name__ == "__main__":
    matrix = [[1]]
    s = Solution()
    a = s.uniquePathsWithObstacles(matrix)
    print(a)

