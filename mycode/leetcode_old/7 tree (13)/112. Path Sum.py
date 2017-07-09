# -*- encoding: utf-8 -*-
# 标签：Tree Depth-first Search
# 题目；给一个binary tree和一个sum.问是否有一个path从头到尾是值加起来等于sum
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# root-to-leaf path 5->4->11->2 which sum is 22
# 思路：如果只有root，root=sum？后面用recursion:如果root.left有值，root.left为root，他这根的值=sum-root.val? 同理root.right

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        if root.left==None and root.right==None and root.val==sum:
            return True
        if root.left!=None:        #如果root.left有值，root.left为root，他这根的值=sum-root.val
            if self.hasPathSum(root.left,sum-root.val)==True:
                return True
        if root.right!=None:     #同理root.right
            if self.hasPathSum(root.right,sum-root.val)==True:
                return True
        return False