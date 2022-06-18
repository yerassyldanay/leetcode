# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if hasattr(root, "left") and root.left:
            if root.left.val >= root.val:
                return False

            if not self.isValidBST(root.left):
                return False

        if hasattr(root, "right") and root.right:
            if root.right.val <= root.val:
                return False

            if not self.isValidBST(root.right):
                return False

        return True

"""
    Example 1:
    
        2
       / \
      1   3
    
    Input: [2,1,3]
    Output: true
    Example 2:
    
        5
       / \
      1   4
         / \
        3   6
    
    Input: [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
"""
