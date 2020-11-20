# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution:
    def reverseBetween(self, node: ListNode, m: int, n: int) -> ListNode:

        if not node or not node.next:
            return node

        pivot = None

        for i in range(1, m):
            if pivot:
                pivot = pivot.next
            else:
                pivot = node

        if pivot:
            temp = pivot.next
        else:
            temp = node

        tail = temp
        head = temp.next

        for i in range(m, n):
            hold = head.next
            head.next = tail
            tail = head
            head = hold

        if pivot:
            pivot.next = tail

        temp.next = head

        if pivot:
            return node
        return tail

temp = ListNode(5, None)
temp = ListNode(4, temp)
# temp = ListNode(3, temp)
# temp = ListNode(2, temp)
# temp = ListNode(1, temp)

s = Solution()
node = s.reverseBetween(temp, 1, 2)

print(node)

while node != None:
    print(node.val, end=" ")
    node = node.next

