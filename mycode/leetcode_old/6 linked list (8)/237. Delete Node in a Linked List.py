# 2级
# -*- encoding: utf-8 -*-
# 题目:给一个linked list,要delete值为val的点
#Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3,
# the linked list should become 1 -> 2 -> 4
# 思路:node这个点的val等于下一点的val,这个点的next等于下一个点的next,这就相当于把这个点去掉

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val  #node这个点(这个位置)的val等于下一点的val
        node.next = node.next.next  #这个点的next等于下一个点的next

#我想用这个方法,但是head是没有给

def deleteNode(node):   #这里一般都是head而不是node所以后边直接用head才不像
    result = ListNode(0)
    cur = result
    result.next = head
    cur.next = head
    while cur.next:
        if cur.next.val == node.val:
            cur.next = cur.next.next
        cur = cur.next
    return result.next