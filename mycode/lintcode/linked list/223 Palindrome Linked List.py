# -*- encoding: utf-8 -*-
# 设计一种方式检查一个链表是否为回文链表。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 1->2->1 就是一个回文链表。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 正确方法
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        if head is None or head.next is None:
            return True
        #找中点
        mid = self.find_mid(head)
        # 分left,right 两部分
        right = mid.next
        right = self.reverse(right)      #注意不能直接写成self.reverse(right)
        mid.next = None
        left = head

        #检查每一个node.val
        while left is not None and right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    def find_mid(self, head):
        # Write your code here
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow


    def reverse(self, head):
        # write your code here
        pre = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
# 快慢指针走，慢的边走边把值存入stack。
# 快的到头时，stack存了前一半的值，慢指针继续往下走，边走边往外pop
# 最后都pop没了就是panlin.
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fast = head
        slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next  #让出中间点
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True
#leet方法：
class Solution1(object):
    def isPalindrome(self, head):
        if not head or not head.next: return True
        length = 0
        fast = head
        end = head
        #算长度
        while fast:
            fast = fast.next
            length = length + 1
        # 取长度的一半，end遍历到中间点
        for i in range(length/2):
            end = end.next
        #从中间点开始，end遍历到底，并翻转箭头，prev是翻转后的头
        prev = None
        while end:
            temp = end.next
            end.next = prev
            prev = end
            end = temp
        # end为另一边的头
        end = prev
        #end和head从两边往中间走。如果值不一样，就不是palindrome
        while end:
            if head.val != end.val:
                return False
            head, end = head.next, end.next
        return True
if __name__ == '__main__':

    P = ListNode(10)
    P.next = ListNode(2)
    P.next.next = ListNode(10)
    # P.next.next.next = ListNode(7)
    # P.next.next.next.next = ListNode(8)
    # P.next.next.next.next.next = ListNode(10)
    s = Solution1()
    print s.isPalindrome(P)