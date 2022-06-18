from typing import List
from collections import defaultdict as dd

class Solution:

    def __init__(self):
        self.bought = dd()
        self.sold = dd()

    def maxProfit(self, k: int, prices: List[int]) -> int:
        mprof = self.buy(k, 0, prices)

        if mprof == float("-inf"):
            return 0
        return mprof

    def buy(self, k, pivot, prices):
        if k == 0:
            return 0

        # may or may not sell
        # cannot but if cannot sell
        # len of prices < 2
        if len(prices[pivot:]) < 2:
            return 0

        # does not buy and sell
        mprof = 0

        for i in range(pivot, len(prices)):
            if i in self.bought:
                temp = self.bought[i]
            else:
                boughtAt = prices[i]
                soldAt = self.sell(k - 1, i + 1, prices)
                temp = soldAt - boughtAt
                self.bought[i] = temp

            mprof = max(mprof, temp)

        return mprof

    def sell(self, k, pivot, prices):
        if pivot >= len(prices):
            return float("-inf")

        # cannot sell then -inf
        # len == 1 > then sell
        if len(prices) - 1 == pivot:  # the last chance to sell
            return prices[pivot]

        mprof = prices[-1]  # have to sell at some point

        for i in range(pivot, len(prices) - 1):
            if i in self.sold:
                temp = self.sold[i]
            else:
                soldAt = prices[i]
                nextProf = self.buy(k, i + 1, prices)
                temp = soldAt + nextProf
                self.sold[i] = temp

            mprof = max(mprof, temp)

        return mprof

s = Solution()
# assert s.maxProfit(4, []) == 0
# assert s.maxProfit(4, [1]) == 0
# assert s.maxProfit(4, [4, 3]) == 0
# test_case_1 = s.maxProfit(4, [1, 2, 100])
# print("test_case_1: ", test_case_1)
# assert test_case_1 == 99
# assert s.maxProfit(0, [2, 3, 4]) == 0

import time
start = time.time()
mprof = s.maxProfit(7, [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94])
print(mprof, "done in: ", start - time.time())

print("Test Passed")