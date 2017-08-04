# -*- encoding: utf-8 -*-
# 给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给一棵二叉树 {3,9,20,#,#,15,7} ：
#
#   3
#  / \
# 9  20
#   /  \
#  15   7
# 返回他的分层遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
    # write your code here
        if root is None:
            return []
        result = []
        stack = []
        stack.append(root)
        while stack != []:
            l = len(stack)
            list_level = []
            for i in range(l):
                if stack[0].left:
                    stack.append(stack[0].left)
                if stack[0].right:
                    stack.append(stack[0].right)
                top = stack.pop(0)
                list_level.append(top.val)
            result.append(list_level)
        return result

from Queue import Queue
class Solution2:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
    # write your code here
        if root is None:
            return []
        result = []
        queue = Queue()
        queue.put(root)
        while queue.qsize()>0:#这里不能写成 while queue：
            l = queue.qsize()
            list_level = []
            for i in range(l):
                q = queue.get()
                if q.left:
                    queue.put(q.left)
                if q.right:
                    queue.put(q.right)
                list_level.append(q.val)
            result.append(list_level)
        return result

if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /   \
    #      2     3
    #    /   \
    #  4      5
    #        / \
    #       6   7
    #            \
    #             8
    P = TreeNode(1)
    P.left = TreeNode(2)
    P.left.left = TreeNode(4)
    P.left.right = TreeNode(5)
    P.left.right.left = TreeNode(6)
    P.left.right.right = TreeNode(7)
    P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(3)
    #
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution2()
    print s.levelOrder(P)