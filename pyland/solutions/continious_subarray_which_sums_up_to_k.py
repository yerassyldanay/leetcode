from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        # len == 1

        count = sumof = 0
        pivot = runner = 0

        sumof = nums[0]

        while runner < len(nums):

            # if nums[runner] == k:
            #     count += 1

            if sumof == k:
                count += 1

            if sumof <= k:

                if runner < len(nums) - 1:
                    runner += 1
                    sumof += nums[runner]
                elif pivot < len(nums) - 1:
                    sumof -= nums[pivot]
                    pivot += 1
                else:
                    return count
            else:
                sumof -= nums[pivot]
                pivot += 1

                if pivot > runner:
                    if pivot == len(nums) or runner == len(nums):
                        return count
                    sumof = sumof + nums[pivot] + nums[runner]
                    runner, pivot = pivot, runner

        return count


s = Solution()
a = s.subarraySum([-1, -1, 1], 1)  # 1
print(a)

# [] +
assert 0 == s.subarraySum([], 1)
# [0], 2 +
assert 0 == s.subarraySum([0], 2)
# [3], 1 +
assert 0 == s.subarraySum([3], 1)
# [5, 2, 1] 3 +
a = s.subarraySum([5, 2, 1], 3)
assert 1 == a
# [1], 1 +
assert 1 == s.subarraySum([1], 1)
# k = 0 [1, 2, 3, 4] +
assert 0 == s.subarraySum([1, 2, 3, 4], 0)
# [0, 0, 0] 0 +
print("0: ", s.subarraySum([0, 0, 0], 0))
# [1, 3, 2] 3 +
assert 1 == s.subarraySum([1, 3, 2], 3)
# [-1,-1, 1] 0
assert 1 == s.subarraySum([-1, -1, 1], 0)
# [-1, -1, 1, 1] 0
assert 1 == s.subarraySum([-1, -1, 1, 1], 0)
# [-1,-1, 1] 1
assert 1 == s.subarraySum([-1, -1, 1], 1)


