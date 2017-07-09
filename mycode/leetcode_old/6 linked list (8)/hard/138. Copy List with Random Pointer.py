# -*- encoding: utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        dummy = RandomListNode(0)
        pre = dummy
        # pre = newnNode
        map = {}
        while head is not None:
            if map.has_key(head):
                newNode = map.get(head)
            else:
                newNode = RandomListNode(head.label)
                map[head] = newNode
            pre.next = newNode
            if head.random is not None:
                if map.has_key(head.random):
                    newNode.random = map.get(head.random)
                else:
                    newNode.random = RandomListNode(head.random.label)
                    map[head.random] = newNode.random
            pre = newNode
            head = head.next
        return dummy.next
# 方法2
class Solution2:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)

    def splitList(self, head):
        newHead = head.next
        while head is not None:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next is not None:
                temp.next = temp.next.next
        return newHead

    def copyRandom(self, head):
        while head is not None:
            if head.next.random is not None:
                head.next.random = head.random.next
            head = head.next.next

    def copyNext(self, head):
        while head is not None:
            newNode = RandomListNode(head.label)
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

if __name__ == '__main__':

    P = RandomListNode(1)
    # P.next = RandomListNode(2)
    # P.next.next = RandomListNode(3)
    # P.next.next.next = RandomListNode(4)
    # P.random = P
    # P.next.random = P.next.next
    # P.next.next.random = P.next
    # P.next.next.next.random = None


    s = Solution()
    print s.copyRandomList(P)