# -*- encoding: utf-8 -*-
# 2级
# 标签：Linked List
# 题目：两个linked lists是不是有重复的一段，求那个交点
# A:     a1 → a2  ↘
#                   c1 → c2 → c3
#                 ↗
# B: b1 → b2 → b3
# 思路：把多余的点先去掉，然后同时往后遍历，发现一样是，那个点就是

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA,curB = headA,headB
        lenA,lenB = 0,0
        while curA is not None:     #求len
            lenA += 1
            curA = curA.next
        while curB is not None:     #求len
            lenB += 1
            curB = curB.next
        curA,curB = headA,headB
        if lenA > lenB:             #去掉前面多出来的那些点
            for i in range(lenA-lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                curB = curB.next
        while curB != curA:         #同时往后遍历
            curB = curB.next
            curA = curA.next
        return curA   