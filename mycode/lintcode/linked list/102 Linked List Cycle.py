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
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head is None or head.next is None:
            return False
        fast = head.next
        slow = head
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True