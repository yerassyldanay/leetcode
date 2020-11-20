import sys
from typing import List, Union
from collections import defaultdict as dd

class Solution:
    def __init__(self):
        self.d = dd()

    def solve(self, n: int, nums: List[int]):
        r = self.__help(n, nums) #- 1
        print("r: ", r)

    def __help(self, n: int, nums: List[int]):
        if n == 0:
            return 0

        if n < 0:
            return None

        if n in self.d:
            return self.d[n]

        mval = sys.maxsize
        for num in nums:
            val = self.__help(n - num, nums)
            if val is None:
                continue

            mval = min(mval, val)

        self.d[n] = mval + 1
        return mval + 1


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> Union[int, float]:
        if amount <= 0:
            return 0
        if min(coins) > amount:
            return -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= amount:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1

        return dp[amount]

s = Solution2()
for i in range(0, 20):
    print(i, s.coinChange([1, 2, 5], i))
# print(a)
