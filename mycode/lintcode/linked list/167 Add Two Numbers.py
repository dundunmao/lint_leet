# coding:utf-8
# 你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出两个链表 3->1->5->null 和 5->9->2->null，返回 8->0->8->null
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        # edge case

        # converse the list to number
        num1 = self.converse(l1)
        num2 = self.converse(l2)
        num = num1+num2
        # converse number to list
        dummy = ListNode(0)
        cur = dummy
        length = len(str(num))
        while length!=0:
            value = num%10
            num = num/10
            cur.next= ListNode(value)
            cur = cur.next
            length -= 1
        return dummy.next


    def converse(self, ll):
        # get the length
        cur = ll
        leng = 0
        while cur is not None:
            leng +=1
            cur = cur.next
        cur = ll
        power = leng - 1
        sum = 0
        while cur is not None:
            sum += cur.val*10**power
            power -= 1
            cur = cur.next
        return sum


class Solution_leet(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result = ListNode(-1)
        l = result
        v = 0
        while l1 or l2:
            if not l1:
                l1_val = 0
                l2_val = l2.val
            elif not l2:
                l2_val = 0
                l1_val = l1.val
            else:
                l1_val = l1.val
                l2_val = l2.val
            v += l1_val + l2_val
            if v < 10:
                l.next = ListNode(v)
                v = 0
            else:
                x = (v) % 10
                l.next = ListNode(x)
                v = 1
            l = l.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if v == 1:
            l.next = ListNode(1)

        return result.next
if __name__ == '__main__':

    P = ListNode(2)
    P.next = ListNode(4)
    P.next.next = ListNode(5)
    P.next.next.next = ListNode(5)
    Q = ListNode(5)
    Q.next = ListNode(6)
    Q.next.next = ListNode(4)
    s = Solution_leet()
    # print s.converse(P)
    print s.addTwoNumbers(P,Q)