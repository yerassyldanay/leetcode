class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        numbers = list()
        while head != None:
            numbers.append(head.val)
            head = head.next

        def helper(numbers: list):
            if not numbers:
                return None
            elif len(numbers) == 1:
                return TreeNode(numbers[0])

            center = len(numbers) // 2
            node = TreeNode(numbers[center])
            node.left = helper(numbers[:center])
            node.right = helper(numbers[center+1:])

            return node

        a = helper(numbers)
        return a

if __name__ == '__main__':
    node = ListNode(-10)
    temp = node
    temp.next = ListNode(-3)
    temp = temp.next
    temp.next = ListNode(0)
    temp = temp.next
    temp.next = ListNode(5)
    temp = temp.next
    temp.next = ListNode(9)

    s = Solution()
    s.sortedListToBST(node)
