# coding: utf-8
# 翻转链表中第m个节点到第n个节点的部分
#
#  注意事项
#
# m，n满足1 ≤ m ≤ n ≤ 链表长度
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出链表1->2->3->4->5->null， m = 2 和n = 4，返回1->4->3->2->5->null
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if head is None or m >= n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        # find the position of pre_m
        for i in range(1, m):
            if pre is None:
                return None
            pre = pre.next
        pre_m = pre
        #position for m
        node_m = pre.next
        # position for n
        node_n = node_m
        # position for after n
        post_n = node_m.next
        # reverse m~n
        for j in range(m, n):
            if post_n is None:
                return None
            temp = post_n.next     #记录post_n的位置
            post_n.next = node_n   # post_n往回指
            node_n = post_n        # n 往下走
            post_n = temp          # post_n 往下走
        # connect
        node_m.next = post_n
        pre_m.next = node_n
        # return
        return dummy.next


class Solution1:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if head is None or m >= n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        i = 1
        while i<m:
            pre = pre.next
            i+=1
        pre_m = pre
        node_m = pre_m.next
        node_n = node_m.next
        j = 1
        while j < (n-m):
            temp = node_n.next
            node_n.next = node_m
            node_m = node_n
            node_n = temp
        temp = node_n.next
        temp.next = pre.next
        pre.next = node_n
        return dummy.next

