# coding:utf-8
# 3级
# 题目: Reverse a linked list from position m to n. Do it in-place and in one-pass.
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):# 因为pre是head前面那个点,所以(m-1)
            pre = pre.next    #这样pre就走到了m那点

        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur  #插入
        pre.next = reverse

        return dummyNode.next