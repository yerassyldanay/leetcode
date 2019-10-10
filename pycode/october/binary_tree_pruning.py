# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        if root != None:
            self.does_contain_one(root)
        return root

    def does_contain_one(self, node: TreeNode) -> bool:
        left = False
        right = False

        if node.right != None:
            if self.does_contain_one(node.right):
                right = True
            else:
                node.right = None

        if node.left != None:
            if self.does_contain_one(node.left):
                left = True
            else:
                node.left = None

        return (left or right or node.val == 1)
