# -*- encoding: utf-8 -*-
# 2级
# 标签：Linked List
# 题目：Merge two sorted linked lists and return it as a new list
 #Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
            result = ListNode(-1)     #result指到一个-1的点
            cur = result                 #cur指到result
            while(l1 and l2):
                if l1.val <= l2.val:         #谁小，cur就指谁，
                    cur.next = l1
                    l1 = l1.next #去头
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next             #cur去头了，但是result一直连着呢
            l3 = l1 and l1 or l2             #l3为l1或l2剩下那些点
            cur.next = l3         #cur把剩下那些点也遍历一下
            return result.next