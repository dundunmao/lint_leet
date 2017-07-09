# -*- coding: utf-8 -*-
import heapq
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        mid = self.mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge_sort(left, right)
    def merge_sort(self, head1, head2):
        dummy = ListNode(0)
        cur = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next
    def mid(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
if __name__ == '__main__':

    P = ListNode(5)
    P.next = ListNode(3)
    P.next.next = ListNode(2)
    P.next.next.next = ListNode(4)

    O = ListNode(2)
    O.next = ListNode(4)
    O.next.next = ListNode(6)

    Q = ListNode(7)
    Q.next = ListNode(8)
    Q.next.next = ListNode(9)
    lists = [O, P, Q]
    s = Solution()
    print s.sortList(P)