# -*- encoding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1     #如果左右子树有一个是NONE，那就等于左右子树高度之和+1.因为dep指的是走到那个节点再也没有路了，所以一边走不下去，就要走另一边，并不是一边没有就走完了,之所以是相加关系，是因为有一边是0
        return min(self.minDepth(root.right),self.minDepth(root.left))+1      #左右子树高度最小的那个再+1