from typing import List
from collections import defaultdict as dd


class Solution:
    def __init__(self):
        self.d = dd()

    def find_ways(self, target: int, nums: List[int]):
        r = self.help(target, nums)
        # print(self.d)
        return r

    def help(self, target: int, nums: List[int]):
        if target == 0:
            return 1

        if target < 0:
            return None

        if target in self.d:
            return self.d[target]

        s = 0
        for num in nums:
            r = self.find_ways(target - num, nums)
            if r is None:
                continue

            s = s + r

        self.d[target] = s
        return s


s = Solution()
result = s.find_ways(100, [1, 2, 3])
print("result: ", result)

# 3 [1, 2]
# 1+1+1 1+2 2+1
#               3
#         2 (1)       1 (2)
#    1 (1)      0 (2)           0 (1)
#  1 (0)
#