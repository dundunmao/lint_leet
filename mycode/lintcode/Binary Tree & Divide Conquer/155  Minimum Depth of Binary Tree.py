# coding:utf-8
# 给定一个二叉树，找出其最小深度。
#
# 二叉树的最小深度为根节点到最近叶子节点的距离。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一棵如下的二叉树:
#
#         1
#
#      /     \
#
#    2       3
#
#           /    \
#
#         4      5
#
# 这个二叉树的最小深度为 2


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None and root.right:
            return self.minDepth(root.right) + 1
        if root.right is None and root.left:
            return self.minDepth(root.left) + 1
        if root.right and root.left:
            return min(self.minDepth(root.right),self.minDepth(root.left) ) + 1

class Solution1(object):
    def __init__(self):
        self.res = float('inf')
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = 1
        self.dfs(root, depth)
        return self.res
    def dfs(self, root, depth):
        if root.left and root.right:
            self.dfs(root.left, depth+1)
            self.dfs(root.right, depth+1)
        if root.left:
            self.dfs(root.left, depth+1)
        elif root.right:
            self.dfs(root.right, depth+1)
        else:
            self.res = min(self.res, depth)
            return
if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /   \
    #      2     3
    #    /   \
    #  4      5
    #        / \
    #       6   7
    #            \
    #             8
    P = TreeNode(1)
    P.left = TreeNode(2)
    P.left.left = TreeNode(4)
    P.left.right = TreeNode(5)
    P.left.right.left = TreeNode(6)
    P.left.right.right = TreeNode(7)
    P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(3)
    #
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution1()
    print s.minDepth(P)