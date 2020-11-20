from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return

        left, mid, right = 0, 1, len(nums) - 1

        while left < right:

            if nums[right] == 2:
                right = right - 1
                continue

            if nums[left] == 0:
                left = left + 1
                continue

            if (nums[left] > nums[right]):
                self.swap(left, right, nums)

            elif nums[left] == nums[right]:
                mid = left + 1

                while nums[mid] == 1:
                    if mid == right:
                        return
                    mid = mid + 1

                if mid == right:
                    return

                if nums[mid] == 0:
                    self.swap(left, mid, nums)

                else:
                    self.swap(mid, right, nums)

    def swap(self, l, r, nums: List[int]):
        nums[l], nums[r] = nums[r], nums[l]


s = Solution()
# b = [2, 2, 1, 0, 2, 1, 0, 0]
b = [0, 0, 0 ,0 ,0 ]
a = s.sortColors(b)
print(a, b)
