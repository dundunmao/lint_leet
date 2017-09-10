# -*- encoding: utf-8 -*-
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0

    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        path = []
        self.helper(root, target, path)
        return self.res

    def helper(self, root, target, path):
        if root is None:
            return
        path.append(root.val)
        self.sum_num(path, target)
        self.helper(root.left, target, path)
        self.helper(root.right, target, path)
        path.pop()

    def sum_num(self, path, target):
        # tmp = target
        l = len(path) - 1
        for i in xrange(l, -1, -1):
            target -= path[i]
            if target == 0:
                self.res += 1