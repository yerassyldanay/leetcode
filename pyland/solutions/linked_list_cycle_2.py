
class ListNode:
    def __init__(self, x, next):
        self.x = x
        self.next = next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return None

        d = {head}
        head = head.next

        while head:

            if head in d:
                return head

            d.add(head)
            head = head.next

        return None

two = ListNode(2, None)
root = ListNode(3, two)
temp = ListNode(-4, two)
temp = ListNode(0, temp)
two.next = temp

# temp.next = root
# root.next = temp

print()

s = Solution()
a = s.detectCycle( root )

if a:
    print(a.x)
else:
    print(a)
