# coding:utf-8
# 3级
# 题目: 把一个linked list的每两个node交换位置


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = self, head    #self 假设为head之前的node
        while pre.next and pre.next.next:
            a = pre.next    #a为第一个node
            b = a.next      #b为第二个node
            pre.next, b.next, a.next = b, a, b.next     #pre指向b(第二个node),b指向a(再指回第一个node),a再指回b的下一个(第三个node,就是a在第三个node前)
            pre = a        #pre设到a就是pre在第三个node前
        return self.next   