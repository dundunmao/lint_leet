# coding:utf-8
# 给一棵二叉树，找出从根节点出发的路径中，和最大的一条。
#
# 这条路径可以在任何二叉树中的节点结束，但是必须包含至少一个点（也就是根了）。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出如下的二叉树：
#
#   1
#  / \
# 2   3
# 返回4。(最大的路径为1→3)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
        if root is None:
            return 0
        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)
        # if no negative, root to leaf
        # return max(left, right) + root.val

        # if has negative, root to anynode
        return max(0, max(left,right)) + root.val