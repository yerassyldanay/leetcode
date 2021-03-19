
class Solution:
    def findPaths(self, m: int, n: int, k: int, i: int, j: int) -> int:

        if m == n == 1:
            return 4

        if k == 0:
            return 0

        divisor = int((10 ** 9) + 7)

        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(k + 1)]

        for y in range(m):
            for x in range(n):
                if m == 1:
                    if 0 < x < n - 1:
                        dp[1][y][x] = 2
                    else:
                        dp[1][y][x] = 3
                    continue

                if n == 1:
                    if 0 < y < m - 1:
                        dp[1][y][x] = 2
                    else:
                        dp[1][y][x] = 3
                    continue

                if y == 0 or x == 0 or x == n - 1 or y == m - 1:
                    dp[1][y][x] = 2

        for ik in range(2, k + 1):
            for y in range(m):
                for x in range(n):

                    left = right = up = down = 0

                    # logic
                    if y != 0:
                        up += dp[ik - 1][y - 1][x]


                    if x != 0:
                        left = dp[ik - 1][y][x - 1]

                    if y != m - 1:
                        down = dp[ik - 1][y + 1][x]

                    if x != n - 1:
                        right = dp[ik - 1][y][x + 1]

                    # print(ik, y, x, "left", left, "right", right, "up", up, "down", down)
                    dp[ik][y][x] = (left + right + up + down) % divisor

        for matrix in dp:
            for row in matrix:
                print(row)
            print()

        # print(k + 1, i, j, len(dp), len(dp[0]))
        return sum([dp[ik][i][j] for ik in range(k + 1)])


if __name__ == "__main__":
    test1 = (2, 2, 2, 0, 0)
    test2 = (1, 3, 3, 0, 0)
    test3 = (1, 1, 1, 0, 0)
    s = Solution()
    a = s.findPaths(1, 1, 1, 0, 0)
    print(a)

