# -*- encoding: utf-8 -*-
# 3级
# 标签：Tree Breadth-first Search
# 题目；遍历树，每一层的为list里的一个element，从上到下
# Given binary tree
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 思路：current存每一行的所有node，next存current里的所有node的左右子节点，result把每次的都存进去积累所有的node
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def levelOrder(self, root):
        result,next=[],[]
        if root:
            current=[root] #temp存每一行的所有node
        else:
            return result  #res把每次的都存进去，积累所有的node
        result.append(current)
        while 1:
            for v in current:
                if v.left:
                    next.append(v.left)    #next存temp里的所有node的左右子节点，
                if v.right:
                    next.append(v.right)
            if next==[]:
                break
            result.append(next)    #把遍历出来的子树存进去
            current=list(next)  #更新为下一行nodes
            next=[]          #清空
        return [[v.val for v in x] for x in result]


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
    P.left.right = Node(6)
    P.right = Node(10)
    P.right.right = Node(4)
    P.right.left = Node(6)
    s = Solution()
    print s.levelOrder(P)