
class Solution:
    def max_subarray_brute_force(self, nums: list) -> int:

        if not nums:
            return 0

        maxv = float("-inf")

        for i in range(len(nums)):
            tmax = 0
            for j in range(i, len(nums)):
                tmax += nums[j]
                maxv = max(maxv, tmax)

        return maxv
    
s = Solution()
a = s.max_subarray_brute_force([1, -1, 2, 3, -5, 5, -1])
print(a)
