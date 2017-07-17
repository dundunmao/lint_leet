# coding: utf-8
# 请写一个程序，找到两个单链表最开始的交叉节点。
#
#  注意事项
#
# 如果两个链表没有交叉，返回null。
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 下列两个链表：
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# 在节点 c1 开始交叉。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# 方法一，让B走到头之后连到A上。这就形成了如103题那样的cycle。然后用103题的方法找到交点的那个node
class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        if headA is None or headB is None:
            return None
        node = headA
        while node.next != None:
            node = node.next
        node.next = headB
        ans = self.listCycle(headA)
        node.next = None
        return ans
    def listCycle(self,head):
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

        while head != slow.next:
            slow = slow.next
            head = head.next
        return head
#方法二：算出两个list的长度，算长度差diff，让长的那个先走diff步，然后两个list一起往后走，遇到相同的node说明相交
class Solution2(object):
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0
        countA, countB = headA, headB
        while countA:
            countA, lenA = countA.next, lenA + 1
        while countB:
            countB, lenB = countB.next, lenB + 1
        for i in range(abs(lenA - lenB)):
            if lenA > lenB:
                headA = headA.next
            else:
                headB = headB.next
        while headA and headB:
            if id(headA) == id(headB):
                return headA
            headA, headB = headA.next, headB.next
        return None

#方法三：两个list同时往后走，走到头再从头走，两人总有一天会相遇。如果俩人不相交，会同时到None
class Solution3:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            if pa is None:
                pa = headB
            else:
                pa = pa.next
            if pb is None:
                pb = headA
            else:
                pb = pb.next

        return pa
#遍历A，存hash key是地址，value是node。再遍历B，看有没有在同一个地址的！
class Solution4:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        if headA is None or headB is None:
            return None
        hash = {}
        while headA != None:
            hash[id(headA)] = headA
            headA = headA.next
        while headB != None:
            if hash.has_key(id(headB)):
                return headB
            else:
                headB = headB.next
        return None

if __name__ == "__main__":

    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    head1 = ListNode(7)
    # head1.next = ListNode(6)
    # head1.next.next = ListNode(5)
    # head1.next.next.next = ListNode(6)
    # head1.next.next.next.next = ListNode(15)
    s = Solution3()
    print s.getIntersectionNode(head,head1)