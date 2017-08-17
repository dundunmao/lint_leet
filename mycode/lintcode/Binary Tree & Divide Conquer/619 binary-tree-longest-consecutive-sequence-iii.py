# coding:utf-8
#  It's follow up problem for Binary Tree Longest Consecutive Sequence II
#
# Given a k-ary tree, find the length of the longest consecutive sequence path.
# The path could be start and end at any node in the tree
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# An example of test data: k-ary tree 5<6<7<>,5<>,8<>>,4<3<>,5<>,3<>>>, denote the following structure:
#
#
#      5
#    /   \
#   6     4
#  /|\   /|\
# 7 5 8 3 5 3
#
# Return 5, // 3-4-5-6-7

class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = [] # children is a list of MultiTreeNode

class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        # Write your code here
        max_len, _, _, = self.helper(root)
        return max_len

    def helper(self, root):
        if root is None:
            return 0, 0, 0
        max_len, up, down = 0, 0, 0
        for child in root.children:
            result = self.helper(child)
            max_len = max(max_len, result[0])
            if child.val + 1 == root.val:
                down = max(down, result[1] + 1)
            if child.val - 1 == root.val:
                up = max(up, result[2] + 1)

        max_len = max(down + 1 + up, max_len)

        return max_len, down, up
if __name__ == '__main__':
    #   2
    #    \
    #     3
    #    /
    #   2
    #  /
    # 1

    P = MultiTreeNode(2)
    P.right = MultiTreeNode(3)
    P.right.left = MultiTreeNode(2)
    P.right.left.left = MultiTreeNode(1)
    # [1,2,3,4,5]
    Q = MultiTreeNode(3)
    Q.left = MultiTreeNode(2)
    # Q.left.left = TreeNode(4)
    # Q.left.right = TreeNode(5)
    Q.right = MultiTreeNode(2)
    # Q.right.right = TreeNode(3)


    s = Solution()
    print s.longestConsecutive3(P)