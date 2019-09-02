class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        result = []
        do_not_repeat = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):

                    if (nums[i] + nums[j] + nums[k]) == 0:
                        key_arr = [nums[i], nums[j], nums[k]]
                        key_arr.sort()

                        if "{}{}{}".format( key_arr[0], key_arr[1], key_arr[2] ) not in do_not_repeat:
                            result.append(
                                key_arr
                            )

                            do_not_repeat["{}{}{}".format( key_arr[0], key_arr[1], key_arr[2] )] = 1

        return result

"""
    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
"""

c = Solution()
print( c.threeSum([-1, 0, 1, 2, -1, -4]) )
