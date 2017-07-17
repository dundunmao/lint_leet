# -*- encoding: utf-8 -*-
# 给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出链表1->2->3->4->5->null和k=2
#
# 返回4->5->1->2->3->null
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # edge case
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        fast = dummy
        slow = dummy
        for_length = head
        # 求出length
        length = 0
        while for_length is not None:
            length += 1
            for_length = for_length.next
        k = k%length    #这里注意要求一个"余".因为可能rotate好几圈
        # fast to the right place
        for i in range(0,k):
            fast = fast.next
        # fast and slow go together
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        # 正确连接上
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next= ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next= ListNode(2)
    s = Solution()
    a = s.rotateRight(head,7)
        