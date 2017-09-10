
# coding:utf-8
#  给一棵二叉树和一个目标值，设计一个算法找到二叉树上的和为该目标值的所有路径。路径可以从任何节点出发和结束，但是需要是一条一直往下走的路线。也就是说，路径上的节点的层级是逐个递增的。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 对于二叉树：
#
#     1
#    / \
#   2   3
#  /   /
# 4   2
# 给定目标值6。那么满足条件的路径有两条：
#
# [
#   [2, 4],
#   [1, 3, 2]
# ]

# DFS
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def __init__(self):
        self.res = []
    def binaryTreePathSum2(self, root, target):
        # Write your code here
        path = []
        self.helper(root, target, path)
        return self.res
    def helper(self, root, target, path):
        if root is None:
            return
        path.append(root.val)
        self.sum_from_end(path,target)
        self.helper(root.left, target, path)
        self.helper(root.right, target, path)
        path.pop()
    def sum_from_end(self,path,target):
        re = []
        for i in range(len(path) - 1, -1, -1):
            target -= path[i]
            if target == 0:
                re.append(i)
        if re == []:
            return
        for i in re:
            p = path[i:]
            self.res.append(p[:])

# BFS
from Queue import Queue


class Solution2:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def __init__(self):
        self.res = []
    def binaryTreePathSum2(self, root, target):
        # Write your code here
        if root is None:
            return []
        q = Queue()
        q.put([root, [root.val]])
        while q.qsize() > 0:
            le = q.qsize()
            for i in range(le):
                [cur, inside_array] = q.get()
                self.sum_from_end(inside_array, target)
                if cur.left:
                    a = inside_array[:]
                    a.append(cur.left.val)
                    q.put([cur.left, a])
                if cur.right:
                    b = inside_array[:]
                    b.append(cur.right.val)
                    q.put([cur.right, b])
        return self.res

    def sum_from_end(self, path, target):
        re = []
        for i in range(len(path) - 1, -1, -1):
            target -= path[i]
            if target == 0:
                re.append(i)
        if re == []:
            return
        for i in re:
            p = path[i:]
            self.res.append(p[:])


if __name__ == '__main__':
    # root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

    #      10
    #     /  \
    #    5   -3
    #   / \    \
    #  3   2   11
    # / \   \
    #3  -2   1

    P = TreeNode(10)
    P.left = TreeNode(5)
    P.left.left = TreeNode(3)
    P.left.left.left = TreeNode(3)
    P.left.left.right = TreeNode(-2)
    P.left.right = TreeNode(2)
    P.left.right.right = TreeNode(1)
    P.right = TreeNode(3)
    P.right.right = TreeNode(11)
    t = 8
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution2()
    print s.binaryTreePathSum2(P,t)
    # [[5, 3], [5, 2, 1]]
