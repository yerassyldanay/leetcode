
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        result = []
        for possib in self.allPossibleFBT_Help(N):
            result.append(possib)
        return result

    def allPossibleFBT_Help(self, N):
        if N == 0:
            return []

        all_possiblities = []

        for i in range(N - 1):
            left = self.allPossibleFBT_Help(i)
            right = self.allPossibleFBT_Help(N - i)

            if len(left) > len(right):
                length = len(left)
            else:
                length = len(right)

            for i in range(length):
                root_node = TreeNode(0)
                if i < len(left):
                    root_node.left = left[i]

                if i < len(right):
                    root_node.right = right[i]

                all_possiblities.append(root_node)
                del root_node

        return all_possiblities

    def convert_bt_to_list(self, root: TreeNode):
        if root == None:
            return []

        tree_dict = {}
        result = []
        tree_dict = self.convert_bt_to_list_help(root, tree_dict, 1)
        for key, value in tree_dict.items():
            # print("key: ", key + " && value: ", value)
            result = result + value

        return [0] + result

    def convert_bt_to_list_help(self, root: TreeNode, tree_dict: dict, level_of_depth: int):
        if f"{level_of_depth}" not in tree_dict:
            tree_dict[f"{level_of_depth}"] = list()

        if root.left != None:
            tree_dict[f"{level_of_depth}"].append(0)
            tree_dict = self.convert_bt_to_list_help(root.left, tree_dict, level_of_depth + 1)
        else:
            tree_dict[f"{level_of_depth}"].append(None)

        if root.right != None:
            tree_dict[f"{level_of_depth}"].append(0)
            tree_dict = self.convert_bt_to_list_help(root.right, tree_dict, level_of_depth + 1)
        else:
            tree_dict[f"{level_of_depth}"].append(None)

        return tree_dict
#
# a = TreeNode(0)
# b = TreeNode(0)
# c = TreeNode(0)
# d = TreeNode(0)
# e = TreeNode(0)
#
# d.left = e
# a.right = d
# b.left = c
# a.left = b
#
s = Solution()
# print(s.convert_bt_to_list(a))
a = s.allPossibleFBT(3)
print(a)