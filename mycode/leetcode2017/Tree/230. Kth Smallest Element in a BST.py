# -*- encoding: utf-8 -*-
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ? k ? BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
# How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
# 方法一： recursive
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return
        s_l = self.size(root.left)
        if s_l == k - 1:
            return root.val
        if s_l > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - s_l - 1)

    def size(self, root):
        if not root:
            return 0
        l = self.size(root.left)
        r = self.size(root.right)
        return l + r + 1
# 方法二 inorder 遍历
class Solution1(object):
    def __init__(self):
        self.count = float('inf')
        self.v = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return
        self.count = k
        self.inorder(root, k)
        return self.v
    # def inorder(self, root, k):  #这种divide&conquer遍历占用额外空间
    #     if root is None:
    #         return []
    #     l = self.inorder(root.left,k)
    #     r = self.inorder(root.right,k)
    #     return l+root.val+r
    def inorder(self, root, k):
        if root.left and self.count >0:
            self.inorder(root.left,k)
        self.count -= 1
        if self.count == 0:
            self.v = root.val
            return
        if root.right and self.count >0:
            self.inorder(root.right,k)
# 方法二 inorder 遍历,o(1)space
class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return
        return self.inorder(root,k)
    def inorder(self, root,k):
        # write your code here
        if root is None:
            return []
        stack = []
        result = 0
        cur = root
        count = 0
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result = cur.val
            count +=1
            if count == k:
                return result
            cur = cur.right
        return None

if __name__ == "__main__":
#      6
#    /  \
#  4    10
# /  \  /
#1   5 8

    P = TreeNode(6)
    P.left = TreeNode(4)
    P.left.left = TreeNode(1)
    P.left.right = TreeNode(5)
    P.right = TreeNode(10)
    P.right.left = TreeNode(8)
    k = 2
    s = Solution1()
    print s.kthSmallest(P,k)