from typing import List
from collections import defaultdict as dd

class Solution:
    def __init__(self):
        self.d = dd()

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.jump(len(cost), cost)

    def jump(self, n: int, cost: List[int]) -> int:
        if n == 0 or n == 1:
            return 0

        if n not in self.d:
            self.d[n] = min(self.jump(n - 1, cost) + cost[n - 1], self.jump(n - 2, cost) + cost[n - 2])

        return self.d[n]

s = Solution()
a = s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(a)
