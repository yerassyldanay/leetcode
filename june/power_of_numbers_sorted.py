from typing import List
from collections import defaultdict as dd

class Solution:
    def getKth(self, lo: int, hi: int, k: int):
        result = []
        dp = dd()

        def help(i: int):

            if i == 1:
                return 1

            if i % 2 == 0:
                ti = i // 2
            else:
                ti = i * 3 + 1

            if ti in dp:
                return dp[ti]

            t = help(ti) + 1
            dp[ti] = t

            return t

        for i in range(lo, hi + 1):
            # val = help(i) - 1
            result.append(i)

        result = sorted(result, key=help)
        # print("dp: ", dp)
        # print(result)

        return result[k-1]


lo = 1
hi = 1000
k = 777

s = Solution()
b = s.getKth(lo, hi, k)
print(b)

