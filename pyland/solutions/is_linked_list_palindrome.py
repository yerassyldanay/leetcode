# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, node):
        self.val = x
        self.next = node

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True

        count = 0
        lead = head

        while lead != None:
            count += 1
            lead = lead.next

        if count == 1:
            return True

        lead = head
        head = head.next

        if count == 2:
            return head.val == lead.val
        elif count == 3:
            return head.next.val == lead.val

        i = 1
        while i < (count // 2):
            temp = head.next
            head.next = lead
            lead = head
            head = temp
            i += 1

        if count % 2 == 1:
            head = head.next

        while head != None:
            if head.val != lead.val:
                return False
            head = head.next
            lead = lead.next

        return True


s = Solution()
temp = ListNode(2, None)
temp = ListNode(2, temp)
temp = ListNode(1, temp)
print(s.isPalindrome(temp))