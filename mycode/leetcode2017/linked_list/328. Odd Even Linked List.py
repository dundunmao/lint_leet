# -*- encoding: utf-8 -*-

# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head