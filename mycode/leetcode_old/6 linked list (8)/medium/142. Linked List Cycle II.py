# coding:utf-8
# 3级
# 题目: 如果一个linked list是cycle的,找到cycle的起点
#         slow 走 H+D, fast是slow的两倍:2(H+D).
#         H: distance from head to cycle entry E
#         D: distance from E to X
#         L: cycle length   _____
#                          /     \
#         head_____H______E       \
#                         \       /
#                          X_____/
#  因为fast应该走H+D+nL-1(因为起点是head.next)所以2H + 2D = H + D + nL-1 --> H = nL - D-1
#  所以如果一个从head走,一个从x走,他们会同时在E相遇
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        try:
            fast = head.next    #这里用next是因为不能让 fast=slow
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            return None
        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next     #因为H = nL-D-1,
        while head is not slow:
            head = head.next
            slow = slow.next
        return head.val
if __name__ == '__main__':
    P = Node(1)
    P.next = Node(2)
    P.next.next = Node(3)
    P.next.next.next = Node(2)
    P.next.next.next.next = Node(5)
    P.next.next.next.next.next = P.next.next
    s = Solution()
    print s.hasCycle(P)