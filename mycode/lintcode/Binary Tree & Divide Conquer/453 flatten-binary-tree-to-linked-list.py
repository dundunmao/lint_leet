# coding:utf-8
#  将一棵二叉树按照前序遍历拆解成为一个假链表。所谓的假链表是说，用二叉树的 right 指针，来表示链表中的 next 指针。
#
#  注意事项
#
# 不要忘记将左儿子标记为 null，否则你可能会得到空间溢出或是时间溢出。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
#               1
#                \
#      1          2
#     / \          \
#    2   5    =>    3
#   / \   \          \
#  3   4   6          4
#                      \
#                       5
#                        \
#                         6

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if root == None:
            return
        self.flatten(root.left)  #左边变成flatten的
        self.flatten(root.right) #右边变成flatten的
        p = root                 #给一个dummy指针指向root
        if p.left == None:       # 如果root的左边是None,这个树就已经flatten好了
            return
        p = p.left                #如果不是，就来的root的左边，
        while p.right:           #一直遍历到左边的最后一个点，
            p = p.right
        p.right = root.right     #把最后一个点跟root的右边连上
        root.right = root.left   #再把左边换到右边
        root.left = None          #再让左边为空