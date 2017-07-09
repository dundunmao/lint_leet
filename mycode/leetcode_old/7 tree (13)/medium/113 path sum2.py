# -*- encoding: utf-8 -*-
# 标签：Tree Depth-first Search
# 题目；给一个binary tree和一个sum.find all root-to-leaf paths where each path's sum equals the given sum.
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# def pathSum(root, sum):
#     if not root: return []
#     if root.left == None and root.right == None:
#         if sum == root.val:
#             return [[root.val]]
#         else:
#             return []
#     a = pathSum(root.left, sum - root.val) + pathSum(root.right, sum - root.val)
#     return [[root.val] + i for i in a]  #i是list,[root.val]+i是list合并
def pathSum(root, sum):
    stack = []   # 每次存路径的
    res = []     #如果路径成果,就作为一个element存这里
    def search(root, sum):
        if (root == None) or (root.val > sum):
            return
        stack.append(root.val)
        if (root.left == None) and (root.right == None):
            if root.val == sum:
                res.append(list(stack)) #如果路径成果,就作为一个element存这里
        else:
            search(root.left, sum - root.val)
            search(root.right, sum - root.val)
        stack.pop()  #往回退的时候,要pop出之前存的那个node值.
    search(root, sum)
    return res

if __name__ == '__main__':
     #        TREE 1
     # Construct the following tree
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
    sum = 22
    P = Node(5)
    P.left = Node(4)
    P.left.left = Node(11)
    P.left.left.left = Node(7)
    P.left.left.right = Node(2)
    P.right = Node(8)
    P.right.right = Node(4)
    P.right.right.right = Node(1)
    P.right.right.left = Node(5)
    P.right.left = Node(13)
    print pathSum(P, sum)