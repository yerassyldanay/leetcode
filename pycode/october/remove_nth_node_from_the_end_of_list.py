# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n):
        if head == None:
            return head
        elif n == 1:
            head = head.next
            return head
        
        first = head
        fcount = 0
        last = head

        index = 0
        while last.next != None:
            index = index + 1
            if index > 2:
                first = first.next
                fcount = fcount + 1

            last = last.next
