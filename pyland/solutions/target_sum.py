from functools import lru_cache
from typing import List

# @lru_cache
def factorial(n: int):
    prod = 1
    for i in range(1, n + 1):
        prod *= i

    return prod


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        maxv = sum(nums)

        if target > maxv or target < -maxv:
            return 0

        dp = [[0] * (maxv * 2 + 1) for _ in range(len(nums))]

        for y in range(len(dp)):
            if y == 0:
                dp[y][maxv + nums[y]] += 1
                dp[y][maxv - nums[y]] += 1
                continue

            for x, counted in enumerate(dp[y - 1]):
                if not counted:
                    continue

                dp[y][x + nums[y]] += counted
                dp[y][x - nums[y]] += counted

        # print(list(range(maxv * 2 + 1)))
        print([abs(x) for x in range(-maxv, maxv + 1, 1)])
        for row in dp:
            print(row)

        # print("target:", dp[len(nums) - 1][maxv + target])

        return dp[len(nums) - 1][maxv + target]


if __name__ == "__main__":
    s = 1
    nums = [0,0,0,0,0,0,0,0,1]
    sol = Solution()
    a = sol.findTargetSumWays(nums, s)
    print(a)

