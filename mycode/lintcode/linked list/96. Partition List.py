# -*- encoding: utf-8 -*-
# 给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。
#
# 你应该保留两部分内链表节点原有的相对顺序。
#
#
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给定链表 1->4->3->2->5->2->null，并且 x=3
#
# 返回 1->2->2->4->3->5->null


# 3级
# 标签：Linked List
# 题目：给一个linked lists和一个value,使比value大或等于的都跑到比value小的后面
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
# 思路:
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def partition(self, head, x):
        if head is None:
            return None
        small = ListNode(0)
        dummy1 = small
        big = ListNode(0)
        dummy2 = big
        while head is not None:
            if head.val < x:
                small.next = head
                small = small.next
                head = head.next
            else:
                big.next = head
                big = big.next
                head = head.next
        # dummy.next = small
        big.next = None    #这句别忘啦!!!!!!
        small.next = dummy2.next
        return dummy1.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next= ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next= ListNode(2)
    s = Solution()

    a = s.partition(head,3)
    print a