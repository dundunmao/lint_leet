# coding:utf-8
#  Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
#
#  注意事项
#
# LintCode will print the subtree which root is your return node.
# It's guaranteed that there is only one subtree with maximum average.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# Given a binary tree:
#
#      1
#    /   \
#  -5     11
#  / \   /  \
# 1   2 4    -2
# return the node 11.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    def __init__(self):
        self.ave = float('-inf')
        self.nod = None

    def findSubtree2(self, root):
        self.helper(root)
        return self.nod

    def helper(self, root):
        if root is None:
            return 0, 0, 0
        l_sum, l_num, l_ave = self.helper(root.left)
        r_sum, r_num, r_ave = self.helper(root.right)
        sumi = l_sum + r_sum + root.val
        num = l_num + r_num + 1.0
        ave = sumi / num
        if ave > self.ave:
            self.ave = ave
            self.nod = root
        return sumi, num, ave