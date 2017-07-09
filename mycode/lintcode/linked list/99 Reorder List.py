# -*- encoding: utf-8 -*-
# 给定一个单链表L: L0→L1→…→Ln-1→Ln,
#
# 重新排列后为：L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 必须在不改变节点值的情况下进行原地操作。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出链表 1->2->3->4->null，重新排列后为1->4->2->3->null。
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if head is None or head.next is None:
            return None
        mid = self.find_mid(head)
        tail = self.reverse(mid.next)
        mid.next = None
        self.merge(head, tail)

    def find_mid(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def merge(self, head1, head2):
        index = 0
        dummy = ListNode(0)
        while head1 is not None and head2 is not None:
            if index % 2 == 0:
                dummy.next = head1
                head1 = head1.next
            else:
                dummy.next = head2
                head2 = head2.next
            dummy = dummy.next
            index += 1
        if head1 is not None:
            dummy.next = head1
        else:
            dummy.next = head2



# 我的练习
class Solution1:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        # edge case
        if head is None or head.next is None:
            return head
        # divide to two
        left, right = self.divide(head)

        # reverse the right part
        reverse_right = self.reverse(right)

        # merge together
        dummy = ListNode(0)
        cur = dummy
        while left is not None and reverse_right is not None:
            cur.next = left
            left = left.next
            cur = cur.next
            cur.next = reverse_right
            reverse_right = reverse_right.next
            cur = cur.next
        if left is not None:
            cur.next = left
        return dummy.next

    def divide(self,head):

        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        head1 = head
        return head1, head2
    def reverse(self,head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        flag = cur
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        flag.next = None
        return pre
if __name__ == "__main__":
    head = ListNode(0)
    head.next = ListNode(3)
    head.next.next= ListNode(1)
    head.next.next.next = ListNode(-1)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next= ListNode(2)
    s = Solution1()
    #test def merge
    head1 = ListNode(3)
    head2 = ListNode(3)
    head2.next = ListNode(4)

    # d1,d2 = s.divide(head)
    # rev =s.reverse(head)
    a = s.reorderList(head)
    x = a
    while x is not None:
        print x.val
        x = x.next