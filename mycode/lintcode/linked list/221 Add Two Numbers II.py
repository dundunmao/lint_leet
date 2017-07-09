# coding: utf-8
# 假定用一个链表表示两个数，其中每个节点仅包含一个数字。假设这两个数的数字顺序排列，请设计一种方法将两个数相加，并将其结果表现为链表的形式。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 6->1->7 + 2->9->5。即，617 + 295。
#
# 返回 9->1->2。即，912 。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists2(self, l1, l2):
        # Write your code here
        num1 = self.converse(l1)
        num2 = self.converse(l2)
        num = num1+num2
        # converse number to list
        dummy = ListNode(0)
        cur = dummy
        length = len(str(num))-1
        while length!=-1:
            value = num/10**length
            num = num%10**length
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