# -*- encoding: utf-8 -*-
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的距离。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一棵如下的二叉树:
#
#   1
#  / \
# 2   3
#    / \
#   4   5
# 这个二叉树的最大深度为3.
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    # traverse
    def __init__(self):
        self.result = 0
    def maxDepth(self, root):
        self.traverse(root,1)
        return self.result
    def traverse(self, root, depth):
        if root is None:
            return
        if depth > self.result:
            self.result = depth
        if root.left:
            self.traverse(root.left, depth+1)
        if root.right:
            self.traverse(root.right, depth+1)

    # divide&conquer
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1



class Solution3:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        result = [0]       #不想用class variable时,就把result变成一个array,只对array里的第一个数做变化,result不能是int,因为into是值传递,array是reference传递.
        self.traverse(root, 1, result)
        return result[0]

    def traverse(self, root, depth, result):
        if root is None:
            return
        result[0] = max(result[0], depth)
        if root.left:
            self.traverse(root.left, depth + 1, result)
        if root.right:
            self.traverse(root.right, depth + 1, result)


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

    s = Solution3()
    print s.maxDepth(P)