import math
from typing import List

class Solution:
    def print(self, matrix: List[List]):
        for row in matrix:
            print(row)
        print()

    def knightDialer(self, n: int) -> int:
        moves = [(-1, -2), (+1, -2), (+2, -1), (+2, +1), (+1, +2), (-1, +2), (-2, +1), (-2, -1)]

        x_length = 3
        y_length = 4

        dp = [[0] * 10 for _ in range(n + 1)]
        dp[0] = list(range(0, 10))
        pad = {(3, 0): -1, (3, 2): -1, (3, 1): 0, (0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9}

        for length in range(1, n + 1):
            for (y_pos, x_pos), num in pad.items():

                if num == -1:
                    continue

                if length == 1:
                    dp[length][num] = 1
                    continue

                for (x_move, y_move) in moves:
                    y_new = y_move + y_pos
                    x_new = x_pos + x_move

                    if not (0 <= y_new < y_length) or not (0 <= x_new < x_length):
                        continue

                    landed_on = pad[(y_new, x_new)]

                    if landed_on == -1:
                        continue

                    dp[length][num] += dp[length - 1][landed_on]

        # self.print(dp)

        return sum(dp[n]) % (int(math.pow(10, 9)) + 7)


if __name__ == "__main__":
    for i in [1, 2, 3, 4, 5, 3131]:
        s = Solution()
        a = s.knightDialer(i)
        print(i, a)
