# -*- encoding: utf-8 -*-
# 标签：Tree
# 题目；对binary search tree，找最近的共同祖先。自己可以是自己的祖先 例如2 and 8 is 6;2 and 4 is 2
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# 思路：binary search tree定义是root.left比root小，root.right比root大。所以，如果都比root小就往左子树移动，如果都比root大就往右子树移动，直到“不都小”或“不都大”时，那个root就是要找的点。


#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        while root:
            if root.val > p.val and root.val > q.val:    #如果root的值比p,q两点的值都大，就往下移一个点到root.left
                root = root.left
            elif root.val < p.val and root.val < q.val:     #如果root的值比p,q两点的值都小，就往下移一个点到root.right
                root = root.right
            else:
                return root