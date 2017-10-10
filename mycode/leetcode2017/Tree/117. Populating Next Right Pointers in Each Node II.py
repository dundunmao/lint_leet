# -*- encoding: utf-8 -*-
# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
# 跟上一题一模一样。用stack每次往里存一排的，然后连上
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
if __name__ == "__main__":
    strs = "0"
    s = Solution()
    print s.numDecodings(strs)