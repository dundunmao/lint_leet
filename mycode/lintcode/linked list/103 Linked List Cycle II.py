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
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        slow =  head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast == None or fast.next == None:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
