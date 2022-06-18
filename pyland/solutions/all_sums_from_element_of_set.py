from typing import List

class Solution:
    def all_sum(self, arr: List[int]) -> List[int]:

        xlen = sum(arr) + 1
        dp = [False] * xlen
        dp[0] = True

        for elem in arr:
            for j in range(len(dp) -1, -1, -1):
                if j - elem >= 0:
                    dp[j] |= dp[j - elem]

            print(elem, dp)

        print(dp)
        return [i for i in range(0, len(dp)) if dp[i]]

s = Solution()
a = s.all_sum([1, 1, 1, 2])
print(a)
