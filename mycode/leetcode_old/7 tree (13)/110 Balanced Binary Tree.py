# -*- encoding: utf-8 -*-
# 标签：Tree Depth-first Search
# 题目；给一个binary tree,看他是不是height-balanced
# 思路：两个函数，一个算height（递归，自己的左子树的）的一个判断是不是的。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:  #root==None
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))