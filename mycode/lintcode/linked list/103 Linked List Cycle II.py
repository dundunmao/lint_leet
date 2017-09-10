# coding:utf-8
# 弗洛伊德算法，龟兔。
# 给定一个链表，如果链表中存在环，则返回到链表中环的起始节点的值，如果没有环，返回null。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 -21->10->4->5, tail connects to node index 1，返回10
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
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None or head.next is None:
            return None
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
        while head != slow.next:
            head = head.next
            slow = slow.next
        return head
