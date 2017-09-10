# -*- encoding: utf-8 -*-
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 我的方法 用全局变量决定什么时候停
class Solution(object):
    def __init__(self):
        self.flag = False
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.helper(root, sum)
        return self.flag
    def helper(self, root, sum):
        if self.flag == True:
            return
        if root is None:
            return
        if root.left is None and root.right is None and sum == root.val:
            self.flag = True
            return
        self.helper(root.left, sum - root.val)
        self.helper(root.right, sum - root.val)

class Solution_leet(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        #只要一个是true，将永远返回True