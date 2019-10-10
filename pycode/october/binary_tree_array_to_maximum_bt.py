
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: list):
        if len(nums) == 0:
            return None

        maindex = 0
        for i, _ in enumerate(nums):
            if nums[maindex] < nums[i]:
                maindex = i

        root = TreeNode(nums[maindex])
        root.left = self.constructMaximumBinaryTree(nums[:maindex])
        root.right = self.constructMaximumBinaryTree(nums[maindex + 1:])

        return root



