# -*- encoding: utf-8 -*-
# 2.5级 思路懂,不会写
# Definition for singly-linked list.
# 标签：Linked List Two Pointers
# 题目：回文
# 思路：fast，slow，rev一个走到尾一个走到中间一个把头半块的箭头反向了。
# 然后rev和slow分别往下遍历，就是两个人从中间分别往两边走，看每一步的值都一样不。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next      #fast走两步，slow走一步，当fast到尾了，slow正好到中间。rev跟着slow但是rev的箭头方向是反的
            rev, rev.next, slow = slow, rev, slow.next         # rev.next=rev就是要反向遍历，箭头反向指。
            # rev = slow   不能这么写,因为这一步,rev已经变了,
            # rev.next = rev    然后这里"="后面需要的是原来的rev
            # slow = slow.next
        if fast:
            slow = slow.next             # 奇偶
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev