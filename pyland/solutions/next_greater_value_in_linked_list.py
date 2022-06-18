# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.result = []
        self.stack = []

    def nextLargerNodes(self, head: ListNode) -> list:
        self.__recursive(head)
        return self.result[::-1]

    def __recursive(self, head: ListNode) -> None:
        if head == None:
            print("None")
            return

        print(head.val)

        self.__recursive(head.next)

        while len(self.stack) != 0:
            val = self.stack.pop()

            if val > head.val:
                self.result.append(val)
                self.stack.extend([val, head.val])
                break

        if len(self.stack) == 0:
            self.result.append(0)
            self.stack.append(head.val)

        return

head = None
tail = None

a = [2, 1, 5]

for val in a:
    if head == None:
        head = ListNode(val)
        tail = head
    else:
        tail.next = ListNode(val)
        tail = tail.next

s = Solution()
b = s.nextLargerNodes(head=head)
print(b)
