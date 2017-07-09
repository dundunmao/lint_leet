# -*- encoding: utf-8 -*-
# 2级
#  Definition for singly-linked list.
# 标签：Linked List
# 题目：掉sorted list的duplicates
# 例如Given 1->1->2, return 1->2; Given 1->1->2->3->3, return 1->2->3.
# 思路：遍历，当node和node.next值相同，去掉node.next
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        node = head
        while node.next:        #当node的下一个不为空
            if node.val == node.next.val:   #当node和node.next值相同
                node.next = node.next.next  #去掉node.next
            else:
                node = node.next
        return head