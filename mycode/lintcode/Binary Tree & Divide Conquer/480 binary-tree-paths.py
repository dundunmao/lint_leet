# coding:utf-8
#  给一棵二叉树，找出从根节点到叶子节点的所有路径。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出下面这棵二叉树：
#
#    1
#  /   \
# 2     3
#  \
#   5
# 所有根到叶子的路径为：
#
# [
#   "1->2->5",
#   "1->3"
# ]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        if root is None:
            return []
        res = []
        path = []
        self.helper(root,path,res)
        return res
    def helper(self,root,path,res):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            ans = '->'.join([str(i) for i in path])
            res.append(ans)
        # if root.left:
        self.helper(root.left,path,res)
        # if root.right:
        self.helper(root.right,path,res)
        path.pop()

class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here\
        path = []
        if root is None:
            return path
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        for ele in left:
            path.append(str(root.val) + '->' + ele)
        for ele in right:
            path.append(str(root.val) + '->' + ele)
        if len(path) == 0:
            path.append('' + str(root.val))
        return path
