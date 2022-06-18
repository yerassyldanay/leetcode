from typing import List

class Solution:
    def longest(self, arr: List[int]) -> int:
        result = [0] * len(arr)

        for i, elem in enumerate(arr):
            t = [result[j] for j in range(0, i) if arr[j] <= elem]
            t = t if t else [0]
            result[i] = max(t) + 1

        print(result)
        return max(result)


# [1, 3, 4, 2, 5]
# [1, 2, 3, 2, 4]

s = Solution()
s.longest([1, 3, 4, 2, 5])
