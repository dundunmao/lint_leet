# -*- encoding: utf-8 -*-
# 3级
# 标签：Tree Depth-first Search
# 题目；是不是对称的树
# 思路：往stack里存node。先存root的左右孩子为一个element，然后pop出去，检查被pop出来的符合（两个node.val一样，或者都是空，后者一空一不空）的条件不。
# 然后存（左左，右右）和（左右，右左）两个element，然后分别pop出去，直到循环到都是空。

# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetric(self, root):
        if root is None:     # 如果root是none
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:    #如果只有root这一个node就进入下一个循环,然后stack就空了,就跳出
                continue
            elif left is None or right is None:     #如果两个中只有一个是none, false
                return False
            elif left.val != right.val:               #如果两个值不一样
                return False
            else:
                stack.append((left.left, right.right))  #左左,右右压进一个element;每次都是检查这一对一不一样
                stack.append((left.right, right.left))  #左右,右左再压进一个element;每次都是检查这一对一不一样

        return True
if __name__ == '__main__':
     #        TREE 1
     # Construct the following tree
     #          26
     #        /   \
     #      10     10
     #    /    \   /  \
     #  4      6   6   4

    P = Node(26)
    P.left = Node(10)
    P.left.left = Node(4)
    P.left.left.left = Node(3)
    P.left.right = Node(6)
    P.right = Node(10)
    P.right.right = Node(4)
    # P.right.right.right = Node(3)
    P.right.left = Node(6)
    s = Solution()
    print s.isSymmetric(P)