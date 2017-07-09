# coding: utf-8
# 删除链表中等于给定值val的所有节点。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5。
#  class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next