# coding:utf-8

# 检查两棵二叉树是否等价。等价的意思是说，首先两棵二叉树必须拥有相同的结构，并且每个对应位置上的节点上的数都相等。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
#     1             1
#    / \           / \
#   2   2   and   2   2
#  /             /
# 4             4
# 就是两棵等价的二叉树。
#
#     1             1
#    / \           / \
#   2   3   and   2   3
#  /               \
# 4                 4
# 就不是等价的。
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # Write your code here
        if a is None and b is None:
            return True
        elif a is None:
            return False
        elif b is None:
            return False
        if a.val != b.val:
            return False
        if not self.isIdentical(a.left, b.left):
            return False
        if not self.isIdentical(a.right, b.right):
            return False
        return True
