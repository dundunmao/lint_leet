# -*- encoding: utf-8 -*-
# 标签：tree
# 题目；左右子树交换
# 思路：递归。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        else:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.right = left
            root.left = right
            # 或者 root.right, root.left= self.invertTree(root.left),self.invertTree(root.right)
            return root



