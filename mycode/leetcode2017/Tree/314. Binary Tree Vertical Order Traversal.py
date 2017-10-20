# -*- encoding: utf-8 -*-
# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples:
#
# Given binary tree [3,9,20,null,null,15,7],
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
# return its vertical order traversal as:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Given binary tree [3,9,8,4,0,1,7],
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
# return its vertical order traversal as:
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# return its vertical order traversal as:
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def verticalOrder(self, root):
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]
import collections

class Solution1(object):
    def verticalOrder(self, root):
        cols = collections.defaultdict(list)   #这个hash的key是col的index，value是一个array，一次按level存的在这个col上的node.val
        q = collections.deque()
        q.append((root, 0))         #这个queue每次存一层的(node，col_index)
        while len(q) != 0:
            le = len(q)
            for k in range(le):
                cur,i = q.popleft()
                if cur:
                    cols[i].append(cur.val)
                    q.append((cur.left, i - 1))
                    q.append((cur.right, i + 1))

        return [cols[i] for i in sorted(cols)]
if __name__ == '__main__':
    #      3
    #     /\
    #    /  \
    #    9   8
    #   /\  /\
    #  /  \/  \
    #  4  01   7
    P = TreeNode(3)
    P.left = TreeNode(9)
    P.left.left = TreeNode(4)
    P.left.right = TreeNode(0)
    P.right = TreeNode(8)
    P.right.left = TreeNode(1)
    P.right.right = TreeNode(7)
    #
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution1()
    print s.verticalOrder(P)