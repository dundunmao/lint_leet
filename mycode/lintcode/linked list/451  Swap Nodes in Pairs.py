# -*- encoding: utf-8 -*-
# 给一个链表，两两交换其中的节点，然后返回交换后的链表。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 1->2->3->4, 你应该返回的链表是 2->1->4->3。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.nenxt = head
        pre = dummy
        left = head
        right = left.next
        while right is not None:
            # reverse
            temp = right.next
            right.next = left
            # connect   注意这里别忘了.
            pre.next = right
            pre = left
            left.next = temp
            # next step
            if temp is None:
                break
            else:
                left = temp
                right = left.next
        return dummy.next

if __name__ == '__main__':

    P = ListNode(1)
    P.next = ListNode(2)
    P.next.next = ListNode(3)
    P.next.next.next = ListNode(4)
    s = Solution()
    print s.swapPairs(P)