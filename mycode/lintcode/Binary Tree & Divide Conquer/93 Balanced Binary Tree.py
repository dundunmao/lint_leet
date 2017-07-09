# coding:utf-8

# 给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出二叉树 A={3,9,20,#,#,15,7}, B={3,#,20,15,7}
#
# A)  3            B)    3
#    / \                  \
#   9  20                 20
#     /  \                / \
#    15   7              15  7
# 二叉树A是高度平衡的二叉树，但是B不是
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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        validate, height = self.helper(root)
        return validate

    def helper(self,root):
        if root is None:
            return True,0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if not left[0]:                   #左子树平衡
            return False, 0
        if not right[0]:                  #右子树平衡
            return False, 0
        if abs(left[1]-right[1]) > 1:       #高度差
            return False, 0
        else:
            return True, max(left[1],right[1])+1   #高度别忘了+1

