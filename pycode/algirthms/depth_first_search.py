
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, node:TreeNode):
        self.root = node

    def addNodeToTheTree(self, node: TreeNode):
        if self.root == None:
            self.root = node
            return
        self.addNodeHelp(self.root, node)

    def addNodeHelp(self, treeNode: TreeNode, node: TreeNode):
        if treeNode.val == node.val:
            return
        elif treeNode.val > node.val:
            if treeNode.left == None:
                treeNode.left = node
                return
            self.addNodeHelp(treeNode.left, node)
        else:
            if treeNode.val < node.val:
                if treeNode.right == None:
                    treeNode.right = node
                    return
                self.addNodeHelp(treeNode.right, node)

    def getRoot(self):
        return self.root

    def printTree(self, node):
        if node == None:
            return ""
        return self.printTree(node.left) + " " + str(node.val) + " " + self.printTree(node.right)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode, lower = float('-inf'), upper = float('+inf')) -> bool:
            if node == None:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            if not helper(node.right, node.val, upper):
                return False

            if not helper(node.left, lower, node.val):
                return False

            return True

        return helper(root)



# a = TreeNode(5)
# bi = BinaryTree(a)
# bi.addNodeToTheTree(TreeNode(2))
# bi.addNodeToTheTree(TreeNode(3))
# bi.addNodeToTheTree(TreeNode(1))
# bi.addNodeToTheTree(TreeNode(7))
# print(bi.printTree(bi.root))
#
# s = Solution()
# b = s.isValidBST(a)
# print("b: ", b)
