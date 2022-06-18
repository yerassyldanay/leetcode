
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        result = ret
        left_from_previous = 0

        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                val = l1.val + l2.val + left_from_previous
                val, left_from_previous = self.resolve(val)

                result.next = ListNode(val)
                result = result.next

                l1 = l1.next
                l2 = l2.next

            elif l1 != None:
                val = l1.val + left_from_previous
                val, left_from_previous = self.resolve(val)

                result.next = ListNode(val)
                result = result.next

                l1 = l1.next

            elif l2 != None:
                val = l2.val + left_from_previous
                val, left_from_previous = self.resolve(val)

                result.next = ListNode(val)
                result = result.next

                l2 = l2.next

        if left_from_previous > 0:
            result.next = ListNode(left_from_previous)

        return ret.next

    def resolve(self, val):
        if val >= 10:
            return val-10, 1
        return val, 0



if __name__ == '__main__':
    # l1 = ListNode(2)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    #
    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)

    c = Solution()
    l3 = c.addTwoNumbers(l1, l2)