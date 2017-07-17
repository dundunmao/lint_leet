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
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        pre = head
        cur = head.next
        while cur != None:
            temp = cur.next
            # already sorted
            if cur.val >= pre.val:
                pre = cur
                cur = temp
            else:
                # find the insert position
                cur2 = dummy
                while cur2.next.val < cur.val:
                    cur2 = cur2.next
                temp2 = cur2.next
                cur2.next = cur
                cur.next = temp2
                # adjust the pre pointer
                pre.next = temp
                cur = temp
        return dummy.next

