
# -*- encoding: utf-8 -*-
# 给一棵二叉树和二叉树中的两个节点，找到这两个节点的最近公共祖先LCA。
#
# 两个节点的最近公共祖先，是指两个节点的所有父亲节点中（包括这两个节点），离这两个节点最近的公共的节点。
#
# 每个节点除了左右儿子指针以外，还包含一个父亲指针parent，指向自己的父亲。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 对于下面的这棵二叉树
#
#   4
#  / \
# 3   7
#    / \
#   5   6
# LCA(3, 5) = 4
# LCA(5, 6) = 7
# LCA(6, 7) = 7

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
# 因为有parent点了,所以就可以找出一条path,就是一边往parent走一边往path里append root.val
# 然后找到两条path的交点
class Solution:
    """
    @param root: The root of the tree
    @param A and B: Two node in the tree
    @return: The lowest common ancestor of A and B
    """
    def path(self, node):
        list = []
        while node:
            list.append(node)
            node = node.parent
        return list

    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        if root is None:
            return None
        list_A  = self.path(A)
        len_A = len(list_A)
        i = len_A-1
        list_B  = self.path(B)
        len_B = len(list_B)
        j = len_B - 1

        while i>=0 and j>=0:
            if list_A[i] == list_B[j]:
                i-=1
                j-=1
            else:
                return list_A[i+1]
        # for only one node
        return list_A[i+1]

# method to use dictionary to ################
#list_A put in dict
#list_B from leaf to root, search in dict, if has, then it is the cross
def lowestCommonAncestorII(self, root, A, B):
# Write your code here
    dict = {}
    while A is not None:
        dict[A] = True
        A = A.parent

    while B is not None:
        if B in dict:
            return B
        B = B.parent

    return root
