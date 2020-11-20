class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        count = 0
        runner = head

        while runner != None:
            runner = runner.next
            count += 1

        if count:
            return self.__merge_sort(head, count)

    def __merge_sort(self, node: ListNode, n: int):
        if node.next == None:
            return node

        first = node
        second = node

        i = 1
        while i != n // 2:
            second = second.next
            i += 1

        temp = second.next
        second.next = None
        second = temp

        first = self.__merge_sort(first, n // 2)
        second = self.__merge_sort(second, n - (n // 2))

        head = None
        pivot = None
        while first or second:
            if not first:
                val = second.val
                second = second.next

            elif not second:
                val = first.val
                first = first.next

            elif first.val < second.val:
                val = first.val
                first = first.next

            else:
                val = second.val
                second = second.next

            if not head:
                head = ListNode(val)
                pivot = head
            else:
                head.next = ListNode(val)
                head = head.next

        return pivot

head = ListNode(3, ListNode(1, ListNode(2)))

s = Solution()
head = s.sortList(head)

while head != None:
    print(head.val)
    head = head.next

