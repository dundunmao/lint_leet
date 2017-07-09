# -*- encoding: utf-8 -*-
# 标签：Tree Breadth-first Search（stack，recursion）
# 题目；遍历树，每一层的为list里的一个element，从下到上
# 思路：BFS从下到上。用stack。往current里塞node，然后pop出来，每pop一个，就把他的左右子node加入到next里，pop空后，next这个list的val插到result头，next里的node整体加入current.然后继续pop.
# given
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def levelOrderBottom(self, root):
        if root == None:
            return []
        result = []
        current = []
        next = [root, None]   #next初始存root
        while len(next) > 0:
            node = next.pop(0)  #node为从next里pop出的第一个元素
            if node == None: #如果pop出的是None,
                if len(current) > 0:
                    result.insert(0, current) #往result的头上插current
                    cur = []         #current清空
                    next.append(None)   #next填入None,避免len=0
            else:
                current.append(node.val)  #如果pop出的不是None,current填入node的值
                if node.left != None:  #next里面填入左右子树
                    next.append(node.left)
                if node.right != None:
                    next.append(node.right)
        return result