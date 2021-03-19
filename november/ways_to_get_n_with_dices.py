
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # target is too big
        # e.g. cannot get 1 with two dices
        if target > d * f or target < d:
            return 0

        # d = 1
        if d == 1:
            return 1

        dp = [[0] * (target + 1) for _ in range(d + 1)]

        for y in range(d + 1):
            for x in range(target + 1):

                if y == 0 or x == 0:
                    dp[y][x] = 0
                    continue

                if y == 1 or x == y:
                    dp[y][x] = 1
                    continue

                if target < d:
                    dp[y][x] = 0
                    continue

                print(y, " dices & ", x, " is target ")
                print(list(range(1, target - d + 2)))
                for chosen in range(1, target - d + 2):
                    dp[y][x] += dp[y][target - chosen]

        print(0, list(range(target)))
        for i, row in enumerate(dp):
            print(i, row)

        return dp[d][target]


if __name__ == "__main__":
    s = Solution()
    #  d = 2, f = 6, target = 7
    a = s.numRollsToTarget(2, 6, 7)
    print(a)

