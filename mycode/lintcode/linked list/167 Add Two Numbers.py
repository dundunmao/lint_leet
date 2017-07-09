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
if __name__ == '__main__':

    P = ListNode(0)
    P.next = ListNode(1)
    P.next.next = ListNode(5)
    Q = ListNode(0)
    s = Solution()
    print s.converse(P)
    print s.addLists(P,Q)