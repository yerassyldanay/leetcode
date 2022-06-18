
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

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.bstHelp(root, 0)
        return root

    def bstHelp(self, node, from_right_wing: int) -> int:
        if node.right != None:
            from_right_wing = self.bstHelp(node.right, from_right_wing)

        from_right_wing = node.val + from_right_wing
        node.val = from_right_wing

        if node.left != None:
            from_right_wing = self.bstHelp(node.left, from_right_wing)

        return from_right_wing

s = Solution()
root = TreeNode(4)
s.insertIntoBST(root, 6)
s.insertIntoBST(root, 5)
s.insertIntoBST(root, 7)
s.insertIntoBST(root, 8)
s.insertIntoBST(root, 1)
s.insertIntoBST(root, 0)
s.insertIntoBST(root, 2)
s.insertIntoBST(root, 3)

s.bstToGst(root)

