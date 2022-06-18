class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        self.d = {}
        self.mval = float("-inf")
        self.level = 0

        def help(node: TreeNode, level: int) -> bool:
            if not node:
                return True

            if level not in self.d:
                self.d.setdefault(level, 0)

            self.d[level] += node.val

            return help(node.left, level + 1) and help(node.right, level + 1)

        help(root, 1)

        for level, val in self.d.items():
            if val > self.mval:
                self.level = level
                self.mval = val

        print(self.d)

        return int(self.level)

left = TreeNode(-89388, None, TreeNode(-32127))
right = TreeNode(98693)

left = TreeNode(10250, right, left)
# right = TreeNode(0)

left = TreeNode(989, None, left)

s = Solution()
print( s.maxLevelSum(left) )
