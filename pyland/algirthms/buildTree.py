
from pyland.algirthms.depth_first_search import BinaryTree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def build(self, pre: list, inr: list):
        def help(pre: list, inr: list):
            if not inr:
                return None

            node = TreeNode(pre.pop(0))
            ind = inr.index(node.val)

            # print(node.val)
            # print(pre, inr)

            node.left = help(pre, inr[:ind])
            node.right = help(pre, inr[ind + 1:])

            return node

        a = help(pre=pre, inr=inr)
        return a

s = Solution()
b = BinaryTree(s.build([3,9,20,15,7], [9,3,15,20,7], 'neutral'))
b.printTree(b.getRoot())
