# coding: utf-8
# 请写一个程序，找到两个单链表最开始的交叉节点。
#
#  注意事项
#
# 如果两个链表没有交叉，返回null。
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 下列两个链表：
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# 在节点 c1 开始交叉。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        if headA is None or headB is None:
            return None
        curA = headA
        arrayA = ['A']
        curB = headB
        arrayB = ['B']
        while curA is not None:
            arrayA.append(curA.val)
            curA = curA.next
        while curB is not None:
            arrayB.append(curB.val)
            curB = curB.next
        i = len(arrayA) - 1
        j = len(arrayB) - 1
        while i>0 and j>0:
            if arrayA[i] == arrayB[j]:
                i -= 1
                j -= 1
            else:
                return ListNode(arrayA[i+1])
        if i == 0:
            return ListNode(arrayA[1])
        if j == 0:
            return ListNode(arrayB[1])

if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head1 = ListNode(7)
    head1.next = ListNode(6)
    head1.next.next = ListNode(5)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    s = Solution()
    s.getIntersectionNode(head,head1)