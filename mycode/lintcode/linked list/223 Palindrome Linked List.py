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
# 我的练习,转成array
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        if head is None or head.next is None:
            return True
        cur = head
        array = []
        while cur is not None:
            array.append(cur.val)
            cur = cur.next
        leng = len(array)
        i = 0
        j = leng-1
        while i < j:
            if array[i] != array[j]:
                return False
            i += 1
            j -= 1
        return True
# 正确方法
class Solution1:
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

if __name__ == '__main__':

    P = ListNode(10)
    P.next = ListNode(8)
    P.next.next = ListNode(7)
    P.next.next.next = ListNode(7)
    P.next.next.next.next = ListNode(8)
    P.next.next.next.next.next = ListNode(10)
    s = Solution1()
    print s.isPalindrome(P)