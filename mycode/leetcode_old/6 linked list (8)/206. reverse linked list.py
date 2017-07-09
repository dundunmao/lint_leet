# -*- encoding: utf-8 -*-
# 标签：Linked List
# 题目：翻转
# 2.5级 思路懂,不会写
# 思路：一个原L-list,一个新L-list。原list从头开始，每个节点都往新list头插

#主要方法:Iterative
class Solution:
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        last = None
        while head:    # 往new的头接node,这个写法背下来
            curr = head
            head = head.next  #原list去头
            curr.next = last  #新list的第一个头为原list的head,指向空
            last = curr   #吧curr赋给new list
        return last

#Recursion
class Solution2:
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, new=None):
        if not node:
            return new
        n = node.next
        node.next = new
        return self._reverse(n, node)