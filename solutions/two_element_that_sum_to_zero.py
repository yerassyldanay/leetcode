
# class TreeNode:
#     def __int__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findOne(self, arr: list, target: int):
        if len(arr) < 2:
            return None

        left = 0
        right = len(arr) - 1

        while left < right:

            if arr[left] + arr[right] == target:
                return arr[ left ], arr[ right ]

            if arr[left] + arr[right] > target:
                right = right - 1

            else:
                left = left + 1

        return None

s = Solution()
print( s.findOne( [1, 2, 2, 3, 5, 7, 8, 10], 20 ) )

