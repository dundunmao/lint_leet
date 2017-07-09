# -*- encoding: utf-8 -*-
# 标签：Tree Binary Search
# 题目；Given a non-empty binary search tree and a target value(floating point), find the value(unique) in the BST that is closest to the target.
# 一个tree,一个target value, 找到最接近target的那个值。
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        gap = abs(root.val - target)
        ans = root
        while root is not None:
            if root.val == target:
                return root.val
            elif target < root.val:                #如果target比root小,就去左子树找接近的
                if abs(root.val - target) < gap:
                    ans = root
                    gap = abs(root.val - target)
                root = root.left                    #左子树比其小,所有往左边走
            else:
                if abs(root.val - target) < gap:
                    ans = root
                    gap = abs(root.val - target)
                root = root.right                   #右子树比其大,所以往右边走
        return ans.val