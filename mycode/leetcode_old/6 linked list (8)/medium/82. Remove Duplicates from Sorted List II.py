# coding:utf-8
# 3级
# 题目: 已知一个sorted linked list,删除所有有duplicate的number
# 例如Given 1->2->3->3->4->4->5, return 1->2->5; Given 1->1->1->2->3, return 2->3.
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
def deleteDuplicates(head):
    dummy = pre = ListNode(0)
    dummy.next = head
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next
    return dummy.next