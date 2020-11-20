from typing import List

class Solution:
    def maxProfi(self, prices: List[int]):
        mval = self.__help(prices, 1, 0, len(prices) - 1)
        return mval

    def __help(self, prices: List[int], year: int, start: int, end: int):
        if start > end:
            return 0

        forward = self.__help(prices, year + 1, start + 1, end) + (year * prices[start])
        backward = self.__help(prices, year + 1, start, end - 1) + (year * prices[end])
        return max(forward, backward)

s = Solution()
a = s.maxProfi([2, 4, 6, 2, 5])
print(a)