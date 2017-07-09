# -*- encoding: utf-8 -*-
# 3
# 题目:给一个单lined list,让所以奇数点放一起,后面跟着所有偶数点,奇数偶数指的是index不是value (in place)
#       Given 1->2->3->4->5->NULL,
#       return 1->3->5->2->4->NULL
# 思路:odd指向head,然后odd挪到这个点，even指向head.next,然后even挪到这个点。然后head移到第三个点，重复。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            if even:
                head = head.next.next
            else:
                None
        odd.next = dummy2.next   #两块接上

        return dummy1.next
