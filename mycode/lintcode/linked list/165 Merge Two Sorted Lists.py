# coding:utf-8
# 将两个排序链表合并为一个新的排序链表
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        head = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1 is not None:
            head.next = l1
        else:
            head.next = l2
        return dummy.next
