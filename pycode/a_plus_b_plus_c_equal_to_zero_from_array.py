import types
import pprint
import random

class Solution:
    def threeSum(selfself, nums):
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n - 1):
            left = i + 1
            right = n - 1
            x = nums[i]
            while left < right:
                if x + nums[left] + nums[right] == 0:
                    ans.add((x, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif x + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans


s = Solution()

if __name__ == '__main__':
    a = s.threeSum([-1,-1,0,0,1,1,2,3])
    print(a)
