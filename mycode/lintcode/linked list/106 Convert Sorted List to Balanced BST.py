# -*- encoding: utf-8 -*-
# 给出一个所有元素以升序排序的单链表，将它转换成一棵高度平衡的二分查找树
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
#                2
# 1->2->3  =>   / \
#              1   3
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
# 将排序好的链表的每个节点的值存入一个数组中，这样就和convert sorted array to B-BST这道题一样了
# 缺点是需要使用额外的空间
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        num = []
        curr = head
        while curr != None:
            num.append(curr.val)
            curr = curr.next
        return self.createBST(num, 0, len(num) - 1)

    def createBST(self, num, start, end):
        if start > end: return None #到最后剩一个node时，mid = 0，start=0，end=mid-1=-1
        mid = (start + end) / 2
        root = TreeNode(num[mid])
        root.left = self.createBST(num, start, mid - 1)
        root.right = self.createBST(num, mid + 1, end)
        return root
#leet方法，每次找到中点，然后左半recurring，右半recurring
class Solution_leet(object):
    def sortedListToBST(self, head):
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, head
        while fast and fast.next: #找中点
            slow = slow.next
            fast = fast.next.next

        mid = slow.next #中点为slow的下一个
        slow.next = None #分开一半
        root = TreeNode(mid.val) #root为中点
        if head != mid: #如果中点就是头儿，就不用再分左右了
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(mid.next)
        return root
# 九章Python法
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        # write your code here
        res = self.dfs(head)

        return res

    def dfs(self, head):

        if head == None:
            return None

        if head.next == None:
            return TreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = dummy

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        parent = TreeNode(temp.val)

        parent.left = self.dfs(head)
        parent.right = self.dfs(temp.next)

        return parent

#九章java解
class Solution3():
    def __init__(self):
        self.cur = 0
    def bst(self, head, st, ed):
        if st > ed or head == None:
            return None
        mid = st + (ed - st)/2
        left = self.bst(self.cur, st, mid - 1)
        root = TreeNode(self.cur.val)
        self.cur = self.cur.next
        right = self.bst(self.cur, mid + 1, ed)
        root.left = left
        root.right = right
        return root

    def sortedListToBST(self, head):
        if head == None:
            return None
        tmp = head
        n = 0
        while tmp != None:
            n += 1
            tmp = tmp.next
        # global cur
        self.cur = head
        return self.bst(self.cur, 0, n)


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next= ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    s = Solution3()

    print s.sortedListToBST(head)