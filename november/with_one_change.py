class Solution:
    def distance(self, s1: str, s2: str) -> int:
        ylen = len(s1) + 1
        xlen = len(s2) + 1

        dp = [[0] * xlen for _ in range(ylen)]

        for y in range(ylen):
            for x in range(xlen):
                if x == 0:
                    dp[y][0] = y
                elif y == 0:
                    dp[0][x] = x

        for y in range(1, ylen):
            for x in range(1, xlen):
                cost = 0
                if s1[y - 1] != s2[x - 1]:
                    cost = 1

                dp[y][x] = min(dp[y - 1][x] + 1, dp[y][x - 1] + 1, dp[y - 1][x - 1] + cost)

        for row in dp:
            print(row)

        return dp[ylen - 1][xlen - 1]

s = Solution()
a = s.distance("cats", "cat")
print(a)



#                            A                      B                           C
#                 AA        AB        AC       BA      BB      BC          CA      CB          CC
#         AAA AAB AAC  ABA ABB ABC ACA ACB ACC
#                            ABCA
#