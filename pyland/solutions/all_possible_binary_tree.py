
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, n):
        def help(n: int) -> list:
            node = TreeNode(0)
            if n == 1:
                return [node]

            n = n - 1
            count = 1

            result = []

            while n - count >= 0:
                left = help(count)
                right = help(n - count)

                for l in left:
                    for r in right:

                        temp = TreeNode(0)

                        temp.left = l
                        temp.right = r

                        result.append(temp)

                count = count + 2

            return result
        return help(n)

    def printTree(self, root: TreeNode):
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        return result

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(7)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(8)

# root.right.left.left = TreeNode(5.5)
# root.right.left.right = TreeNode(6.5)

s = Solution()
for t in s.allPossibleFBT(7):
    a = s.printTree(t)
    print(a)
    print()

