# coding:utf-8
# 给定一个链表，判断它是否有环。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 -21->10->4->5, tail connects to node index 1，返回 true
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow =  head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False