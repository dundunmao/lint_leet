# -*- encoding: utf-8 -*-
# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
# 用stack每次往里存一排的，然后连上
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #corner case
        if root is None:
            return root

        q =  deque()
        q.append(root)
        while q:
            le = len(q)
            temp = None
            for i in range(le):
                item = q.pop()
                if item.right:
                    q.appendleft(item.right)
                if item.left:
                    q.appendleft(item.left)
                if i == 0:
                    item.next = None
                else:
                    item.next = temp
                temp = item