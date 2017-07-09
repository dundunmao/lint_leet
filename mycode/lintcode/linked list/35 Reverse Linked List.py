# coding:utf-8
# 翻转一个链表
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre