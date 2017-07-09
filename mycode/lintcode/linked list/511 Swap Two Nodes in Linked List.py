# -*- encoding: utf-8 -*-
# 给你一个链表以及两个权值v1和v2，交换链表中权值为v1和v2的这两个节点。保证链表中节点权值各不相同，如果没有找到对应节点，那么什么也不用做。
#
#  注意事项
#
# 你需要交换两个节点而不是改变节点的权值
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出链表 1->2->3->4->null ，以及 v1 = 2 ， v2 = 4
# 返回结果 1->4->3->2->null。


# 先找第一个出现的node,再找第二个.
# 找到后翻转

# 注意
# 1: v1,v2不一定谁在第一个.
# 2: 翻转时讨论两node挨着和不挨着两种情况
# 3: 讨论node不存在的情况

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        # Write your code here
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        # find first node
        pre = dummy
        cur = head
        post = head.next
        first = None
        second = None
        while cur is not None:
            if cur.val == v1 or cur.val == v2:       #找第一个出现的node
                first = cur
                pre_first = pre
                first_next = post
                break
            pre = pre.next
            cur = cur.next
            post = post.next
        # find second node
        pre = dummy
        cur = head
        post = head.next
        if first.val == v1:                      #找后面那个node
            while cur is not None:
                if cur.val == v2:
                    second = cur
                    pre_second = pre
                    second_next = post
                    break
                if post is None:
                    break
                pre = pre.next
                cur = cur.next
                post = post.next
        elif first.val == v2:
            while cur is not None:
                if cur.val == v1:
                    second = cur
                    pre_second = pre
                    second_next = post
                    break
                if post is None:
                    break
                pre = pre.next
                cur = cur.next
                post = post.next


        if first == None or second == None:     #讨论node不存在的情况
            return head


        if first.next == second:                 #讨论俩node挨着的情况
            pre_first.next = second
            second.next = first
            first.next = second_next
        else:                                   # 不挨着的情况
            pre_first.next = second
            second.next = first_next
            pre_second.next = first
            first.next = second_next
        return dummy.next

if __name__ == '__main__':

    P = ListNode(10)
    P.next = ListNode(8)
    P.next.next = ListNode(7)
    P.next.next.next = ListNode(6)
    P.next.next.next.next = ListNode(4)
    P.next.next.next.next.next = ListNode(3)
    s = Solution()
    print s.swapNodes(P,8,10)