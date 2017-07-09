# coding:utf-8

# 给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行）
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一棵二叉树 {3,9,20,#,#,15,7},
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其锯齿形的层次遍历为：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from Queue import Queue

class Solution:
    """
    @param root: The root of binary tree.
    @return: A list of list of integer include
             the zig zag level order traversal of its nodes' values
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if root is None:
            return []
        result = []
        q = Queue()
        q.put(root)
        level = 1
        while q.qsize()>0:
            size = q.qsize()
            path = []
            for i in range(size):
                node = q.get()
                if level%2 == 1:
                    path.append(node.val)
                elif level%2 == 0:
                    path.insert(0,node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            result.append(path)
            level += 1

        return result