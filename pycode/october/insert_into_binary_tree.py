# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        elif val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)

        return root


s = Solution()
root = TreeNode(4)
s.insertIntoBST(root, 2)
s.insertIntoBST(root, 3)
s.insertIntoBST(root, 1)


