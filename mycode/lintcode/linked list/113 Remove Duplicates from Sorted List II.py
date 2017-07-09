# coding:utf-8
# 给定一个排序链表，删除所有重复的元素只留下原链表中没有重复的元素。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 1->2->3->3->4->4->5->null，返回 1->2->5->null
#
# 给出 1->1->1->2->3->null，返回 2->3->null
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
        # write your code here
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next is not None and pre.next.next is not None:
            if pre.next.val == pre.next.next.val:
                val = pre.next.val
                while pre.next is not None and pre.next.val == val:
                    # 把 pre.next 删掉,一直删掉没有node的值为val
                    pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next