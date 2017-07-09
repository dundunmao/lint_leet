# -*- encoding: utf-8 -*-
# 给出一棵二叉树，返回其节点值从底向上的层次序遍历（按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）
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
# 按照从下往上的层次遍历为：
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


from Queue import Queue
class Solution:
    """
    @param root: The root of binary tree.
    @return: buttom-up level order in a list of lists of integers
    """
    def levelOrderBottom(self, root):
        # write your code here
        if root is None:
            return []
        result = []
        queue = Queue()
        queue.put(root)
        while queue.qsize()>0:
            list_level = []
            l = queue.qsize()
            for i in range(l):
                q = queue.get()
                if q.left:
                    queue.put(q.left)
                if q.right:
                    queue.put(q.right)
                list_level.append(q.val)
            result.insert(0,list_level)
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

    s = Solution()
    print s.levelOrderBottom(P)
