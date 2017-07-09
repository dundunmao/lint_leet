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
    # def __init__(self, cur):
    #     self.cur = cur
    # def get_list_len(self, head):
    #     size = 0
    #     while head is not None:
    #         size += 1
    #         head = head.next
    # def sortedListToBST(self, head):
    #     # write your code here
    #     self.cur = head
    #     size = self.get_list_len(head)
    #     return self.sorted_list_helper(size)
    # def get_list_len(self, head):
    #     size = 0
    #     while head is not None:
    #         size += 1
    #         head = head.next
    #     return size
    # def sorted_list_helper(self, size):
    #     if size <= 0:
    #         return None
    #     left = self.sorted_list_helper(size/2)
    #     root = TreeNode(self.cur.val)
    #     self.cur = self.cur.next
    #     right = self.sorted_list_helper(size - 1 - size/2)
    #     root.left = left
    #     root.right = right
    #     return root
    def sortedListToBST(self, head):
        num = []
        curr = head
        while curr != None:
            num.append(curr.val)
            curr = curr.next
        return self.createBST(num, 0, len(num) - 1)

    def createBST(self, num, start, end):
        if start > end: return None
        mid = (start + end) / 2
        root = TreeNode(num[mid])
        root.left = self.createBST(num, start, mid - 1)
        root.right = self.createBST(num, mid + 1, end)
        return root
class Solution2:
    # @param head, a list node
    # @return a tree node
    def bst(self, head, st, ed):
        if st > ed or head[0] == None:
            return None
        mid = st + (ed - st)/2
        left = self.bst(head, st, mid - 1)
        root = TreeNode(head[0].val)
        head[0] = head[0].next
        right = self.bst(head, mid + 1, ed)
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
        return self.bst([head], 0, n)


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