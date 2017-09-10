# coding:utf-8
#  Given a binary tree, find the length of the longest consecutive sequence path.
# 最长连续递增序列
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# For example,
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
# 这道题要求找到二叉树中的最长连续递增序列，其中路径只能从父节点往子节点延伸，即路径只能自上往下走。

# 用递归的方式去分别求得以当前节点左右子树为起点的最长连续递增序列长度，然后比较该节点与其左右子节点是否属于连续递增关系，
# 通过简单的计算便可得知以当前节点为起点的最长连续递增序列长度。同时，用一个全局变量维护已发现的最大长度即可。
# 方法一 traverse
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def __init__(self):
        self.length = 0
    def longestConsecutive(self, root):
        # Write your code here
        if root is None:
            return 0
        le = 0
        pre = None
        self.helper(root,pre,le)
        return self.length
    def helper(self,root,pre,le):
        if root is None:

            return
        if pre != None and root.val == pre.val + 1:
            le += 1
            self.length = max(self.length, le)
        else:
            le = 1
            self.length = max(self.length, le)
        self.helper(root.left, root, le)
        self.helper(root.right, root, le)
        le -= 1

# 方法二 traverse + divide&conquer


class Solution1:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path

    def longestConsecutive(self, root):
        # Write your code here
        if root is None:
            return 0
        le = 0
        pre = None
        return self.helper(root, pre, le)
    def helper(self,root,pre,le):
        if root is None:
            return 0
        if pre != None and root.val == pre.val + 1:
            le += 1
        else:
            le = 1
        l = self.helper(root.left, root, le)
        r = self.helper(root.right, root, le)
        return max(l,r,le)
# 我自己的练习
class Solution1:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        le, con = self.helper(root)
        return le
    def helper(self, root):
        if root is None:
            return 0,0
        if root.left is None and root.right is None:
            return 1,1
        l, con_l = self.helper(root.left)
        r, con_r = self.helper(root.right)
        if root.left and root.left.val - 1 == root.val:
            con_l += 1
        else:
            con_l = 1
        if root.right and root.right.val - 1 == root.val:
            con_r += 1
        else:
            con_r = 1
        return (max(l,r,con_l,con_r),max(con_l,con_r))
if __name__ == '__main__':
    #   2
    #    \
    #     3
    #    /
    #   2
    #  /
    # 1

    P = TreeNode(2)
    P.right = TreeNode(3)
    P.right.left = TreeNode(2)
    P.right.left.left = TreeNode(1)
    # [1,2,3,4,5]
    Q = TreeNode(3)
    Q.left = TreeNode(2)
    # Q.left.left = TreeNode(4)
    # Q.left.right = TreeNode(5)
    Q.right = TreeNode(2)
    # Q.right.right = TreeNode(3)


    s = Solution1()
    print s.longestConsecutive(Q)



