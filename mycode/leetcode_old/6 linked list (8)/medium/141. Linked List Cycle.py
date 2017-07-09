# coding:utf-8
# 3级
# 题目: Given a linked list, determine if it has a cycle in it.(不要用extra space)找是否有circle
#

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast: #当slow和fast不重合的时候,slow一下走一步,fast走两步,重合时结束循环
                slow = slow.next
                fast = fast.next.next
            return True             #返回True
        except Exception, e:  #当fast走到头了,(object has no attribute 'next')while的条件也没达到时,try 部分结束
            print e
            return False

if __name__ == '__main__':
    P = Node(1)
    P.next = Node(2)
    P.next.next = Node(3)
    P.next.next.next = Node(2)
    # P.next.next.next.next = Node(5)
    # P.next.next.next.next.next = Node(2)
    # P.next.next.next.next.next.next = Node(7)
    s = Solution()
    print s.hasCycle(P)