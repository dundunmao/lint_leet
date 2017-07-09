# -*- encoding: utf-8 -*-
# 给一个排序数组（从小到大），将其转换为一棵高度最小的排序二叉树。
#
#  注意事项
#
# There may exist multiple valid solutions, return any of them.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组 [1,2,3,4,5,6,7], 返回
#
#      4
#    /   \
#   2     6
#  / \    / \
# 1   3  5   7
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        if A is None:
            return None
        return self.build_tree(A, 0, len(A)-1)
    def build_tree(self, A, start, end):
        if start > end:
            return None
        node = TreeNode(A[(start+end)/2])
        node.left = self.build_tree(A, start, (start+end)/2-1)
        node.right = self.build_tree(A, (start+end)/2+1, end)
        return node