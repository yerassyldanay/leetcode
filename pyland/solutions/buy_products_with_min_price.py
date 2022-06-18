from typing import List

class Solution:
    def print(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print(row)
        print()

    def minv(self, matrix: List[List[int]]) -> int:
        k = len(matrix)
        d = len(matrix[0])

        total = [[1 << 32 - 1] * d for _ in range(1 << k)]
        self.print(total)

        for i in range(k):
            total[1 << i][0] = matrix[i][0]

        self.print(total)

        for day in range(1, d):
            for comb in range(0, 1 << k, 1):
                total[comb][day] = total[comb][day - 1]
                for prod in range(k):
                    if comb & (1 << prod):
                        total[comb][day] = min(total[comb][day], total[comb ^ (1 << prod)][day - 1] + matrix[prod][day])
                    # print(comb, "&", (1 << prod), comb & (1 << prod))
                # print(comb)
            print()

        self.print(total)

        return 0


if __name__ == "__main__":
    matrix = [[1, 2, 3], [1, 3, 1], [1, 1, 3]]
    s = Solution()
    a = s.minv(matrix)
    print(a)

