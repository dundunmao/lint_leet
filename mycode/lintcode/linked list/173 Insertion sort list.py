# coding: utf-8
# 用插入排序对链表排序
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# Given 1->3->2->0->null, return 0->1->2->3->null
# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 我的方法,超时啦.
class Solution1:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        # dummy = ListNode(-1)
        # dummy.next = head
        cur = head
        while cur.next is not None:
            cur_node = ListNode(cur.next.val)
            # cur.next = None
            self.insert(head,cur_node)
            cur = cur.next.next
        return head

    def insert(self, head, node):
        cur = head
        while cur is not None:
            if cur.val<node.val:
                cur = cur.next
            else:
                cur.next = node
                node.next = cur.next
        return head


# 答案
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(-1)
        # dummy.next = head
        # cur = head
        while head is not None:
            cur = dummy
            while cur.next is not None and cur.next.val < head.val:
                cur = cur.next
            temp = head.next
            head.next = cur.next
            cur.next = head
            head = temp
        return dummy.next