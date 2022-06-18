class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def bstFromPreorder(self, preorder: list):
        if len(preorder) < 1:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])

        parentNode = TreeNode(preorder[0])
        index = 0
        for i, num in enumerate(preorder):
            if num > preorder[index]:
                index = i
                break

        if index == 0:
            left_side = self.bstFromPreorder(preorder[1:])
            parentNode.left = left_side
            return parentNode

        right_side = self.bstFromPreorder(preorder[index:])
        parentNode.right = right_side

        left_side = self.bstFromPreorder(preorder[1:index])
        parentNode.left = left_side

        return parentNode

s = Solution()
root = s.bstFromPreorder([4,2, 3])
print(root)