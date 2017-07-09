# -*- encoding: utf-8 -*-
# 2 级
# 标签：Linked List
# 题目：给定一个值val，把list里所有值为val的去掉,遇到cur.next.val == val,就cur.next = cur.next.next
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(-1)  #标杆，要return它
        dummy.next = head
        cur = dummy       #光标，用来遍历list
        while cur != None and cur.next != None:
            if cur.next.val == val:       #val出现
                cur.next = cur.next.next     #去掉要它
            else:
                cur = cur.next

        return dummy.next