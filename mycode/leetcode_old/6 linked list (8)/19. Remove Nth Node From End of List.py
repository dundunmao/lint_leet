# -*- encoding: utf-8 -*-
# 3级
# 标签：Linked List Two Pointers
# 题目：移除从end数的第n个node，返回head
# 思路：两个pointer,fast,slow，使fast到tail时，slow到想删除的那个数的前一个。然后让slow.next = slow.next.next
class Node(object):
    def __init__(self,data):
        self.val = data
        self.next = None

def removeNthFromEnd(head,n):
    result = Node(0)
    result.next = head
    slow = fast =result
    count = 0
    while fast.next:
        fast = fast.next
        count +=1
        if count>n:
            slow = slow.next
    slow.next = slow.next.next
    return result.next



if __name__ == '__main__':
    P = Node(1)
    P.next = Node(2)
    P.next.next = Node(3)
    P.next.next.next = Node(2)
    P.next.next.next.next = Node(5)
    P.next.next.next.next.next = Node(2)
    P.next.next.next.next.next.next = Node(7)
    print removeNthFromEnd(P,1)
