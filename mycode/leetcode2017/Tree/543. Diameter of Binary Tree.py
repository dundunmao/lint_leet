# -*- encoding: utf-8 -*-
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

#解题： For every node, length of longest path which pass it = MaxDepth of its left subtree + MaxDepth of its right subtree.
# 所以就是走一遍求maxdepth,边走边更新self.max.最后return的就是self.max
class Solution(object):
    def __init__(self):
        self.maxi = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.MaxDepth(root)
        return self.maxi

    def MaxDepth(self, root):  # 不用考虑root = None,因为底下已经考虑了如果左枝或右枝是空就不往那走
        if root.left is None and root.right is None:
            return 0
        if root.left is None:
            left = self.MaxDepth(root.right)
            self.maxi = max(self.maxi, left + 1)
            return left + 1
        elif root.right is None:
            right = self.MaxDepth(root.left)
            self.maxi = max(self.maxi, right + 1)
            return right + 1
        else:
            left = self.MaxDepth(root.right)
            right = self.MaxDepth(root.left)
            self.maxi = max(self.maxi, left + right + 2)
            return max(left, right) + 1

# 或者简化点写，不用判断有没有左右node,如果没有就return -1，这样后面"+2"其实就是"+1"
class Solution(object):
    def __init__(self):
        self.maxi = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.MaxDepth(root)
        return self.maxi

    def MaxDepth(self, root):
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return 0
        left = self.MaxDepth(root.right)
        right = self.MaxDepth(root.left)
        self.maxi = max(self.maxi, left + right + 2)
        return max(left, right) + 1