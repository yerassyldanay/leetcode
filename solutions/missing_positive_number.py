class Solution:
    def firstMissingPositive(self, nums: list) -> int:

        if not nums:
            return 1

        # []
        # [1, 2, 0]
        # [-1, -2, -3]
        # [7, 8, 9]
        # [-1, 4, 3, 1]
        # [-1, -1, -1, -1]
        # [1, 1, 1, 1]

        minv = float("inf")
        maxv = float("-inf")

        for num in nums:
            if minv > num > 0:
                minv = num

            if maxv < num:
                maxv = num

        if minv > 1 or maxv < 1:
            return 1

        if maxv >= len(nums):
            nums.extend([-1] * (maxv - len(nums) + 1))

        print( nums, maxv )

        i = 0
        while i < len(nums):
            if nums[i] < 0 or nums[i] == i:
                i = i + 1
                continue

            # repeating values
            # [1, 1, 2, 5]

            tval = nums[i]

            if tval >= 0 and nums[nums[i]] == nums[i]:
                nums[i] = -1
                continue

            nums[i] = nums[tval]
            nums[tval] = tval

            if nums[i] == i:
                i = i + 1

        for i, num in enumerate(nums):
            if i == 0:
                continue

            if num != i:
                return i

        return len(nums)


s = Solution()
print(s.firstMissingPositive( [3,4,-1,1] ))
