# coding:utf-8
# 给定一个二叉树，找出其最小深度。
#
# 二叉树的最小深度为根节点到最近叶子节点的距离。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一棵如下的二叉树:
#
#         1
#
#      /     \
#
#    2       3
#
#           /    \
#
#         4      5
#
# 这个二叉树的最小深度为 2
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None and root.right:
            return self.minDepth(root.right) + 1
        if root.right is None and root.left:
            return self.minDepth(root.left) + 1
        if root.right and root.left:
            return min(self.minDepth(root.right),self.minDepth(root.left) ) + 1