# -*- encoding: utf-8 -*-
# 给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点。
#
# 返回一个深拷贝的链表。

# 这里只用了一个循环,是一边生成new node,一边生成其random关系.但是老师讲这样不对,因为如果random关系里指向的那个
# node还不存在的话就要生成,而两次生成的点不是同一个点.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
#方法一:用hash,一边查询,一边存储,next和random在同一个循环里进行
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
            if head.random is not None:          #这里别忘了
                if map.has_key(head.random):
                    newNode.random = map.get(head.random)
                else:
                    newNode.random = RandomListNode(head.random.label)
                    map[head.random] = newNode.random
            pre = pre.next            #这里别忘了.
            head = head.next
        return dummy.next

# 方法二,基本同上,但是先循环得到next,再循环一边得到random

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        hash = {None:None}
        dummy1 = RandomListNode(0)
        cur = dummy1
        dummy2 = RandomListNode(0)
        dummy2.next = head

        while head is not None:
            if hash.has_key(head):
                new = hash[head]
            else:
                new = RandomListNode(head.label)
                hash[head] = new
            cur.next = new
            cur = cur.next
            head = head.next
        new = dummy1.next
        old = dummy2.next
        while old is not None:
            new.random = hash[old.random]
            old = old.next
            new = new.next
        return dummy1.next



# 方法3: 先loop一遍,在每一个点后都复制一边这个node 1->1'->2->2'->3->3'->N这时候random都带上
#       再loop一遍,提取每一个新点和起箭头.
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