
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, node: TreeNode) -> list:

        result = []
        stack = list()

        while True:

            while node != None:
                stack.append(node)
                node = node.left

            if not stack:
                return result

            node = stack.pop()
            result.append(node.val)

            node = node.right

temp = TreeNode(3, None, None)
temp = TreeNode(2, temp, None)
temp = TreeNode(1, None, temp)

s = Solution()
print(s.inorderTraversal(temp))

