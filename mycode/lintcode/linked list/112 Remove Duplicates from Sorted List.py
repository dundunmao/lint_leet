# coding:utf-8
# 给定一个排序链表，删除所有重复的元素每个元素只留下一个。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 1->1->2->null，返回 1->2->null
#
# 给出 1->1->2->3->3->null，返回 1->2->3->null
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """

    def deleteDuplicates(self, head):
        if head is None:
            return None
        cur = head
        while cur.next is not None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head