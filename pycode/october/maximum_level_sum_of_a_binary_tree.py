class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        d = {}
        self.maxLevelSumHelp(root, d, 1)
        # print(d)

        ma = -1
        makey = 0
        for key, value in d.items():
            if value > ma:
                makey = key
                ma = value

        return makey

    def maxLevelSumHelp(self, root: TreeNode, d: dict, level: int):
        if root == None:
            return

        if f"{level}" not in d:
            d[f"{level}"] = 0

        d[f"{level}"] = d[f"{level}"] + root.val

        if root.left != None:
            self.maxLevelSumHelp(root.left, d, level + 1)

        if root.right != None:
            self.maxLevelSumHelp(root.right, d, level + 1)

a = TreeNode(989)
b = TreeNode(10250)
c = TreeNode(98693)
d = TreeNode(-89388)
e = TreeNode(-32127)

a.right = b
b.left = c
b.right = d
d.right = e

s = Solution()
aa = s.maxLevelSum(a)
print(aa)
