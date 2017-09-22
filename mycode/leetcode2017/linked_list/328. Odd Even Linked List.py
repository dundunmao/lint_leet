# -*- encoding: utf-8 -*-
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = even
        # 先odd走再even走，每循环一次odd和even都走一次
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

# 下面这种是错的做法没有破坏原来的指针，并没有重新指向
class Solution1(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur_odd = head
        cur_even = head.next
        even = cur_even
        while cur_even and cur_even.next:
            cur_even = cur_even.next.next
        while cur_odd and cur_odd.next:
            pre = cur_odd
            cur_odd = cur_odd.next.next
        if cur_odd:
            cur_odd.next = even
        else:
            pre.next = even
        return head
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next= ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next= ListNode(2)
    s = Solution1()
    s.oddEvenList(head)



