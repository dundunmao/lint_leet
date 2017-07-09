# coding:utf-8
# 3级
# 题目:把一个从小大sorted 的linked list转换成平衡BST(binary search tree)
# recursively
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedListToBST(self,head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2','3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'belongs to left, '3' is root, '45' belongs to right
        slow, fast = head, head.next.next   #这一段在找中点,记下
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next      # tmp points to root
        slow.next = None    # cut down the left child
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root