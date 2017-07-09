
# -*- encoding: utf-8 -*-
# Given a binary tree, find its maximum depth.
# 标签：Tree Depth-first Search
# 题目；二叉树深度
# 思路：递归。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #这里条件别写反了,要先写root,再写root.left,root.right
        if root==None:  # 或者 if not root:
            return 0
        elif root.left ==None and root.right==None:#或者root.left and not root.right:    #有没有这一段都行
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
if __name__=='__main__':
    root = TreeNode(2)
    left = TreeNode(3)
    right = TreeNode(4)
    left_l = TreeNode(5)
    root.left = left
    left.left = left_l
    root.right = right
    s = Solution()
    print s.maxDepth(root)