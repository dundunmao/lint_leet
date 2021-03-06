# coding:utf-8
#  给一棵二叉树和一个目标值，找到二叉树上所有的和为该目标值的路径。路径可以从二叉树的任意节点出发，任意节点结束。
# 这题还提供了parent这个参数
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给一棵这样的二叉树：
#
#     1
#    / \
#   2   3
#  /
# 4
# 和目标值 target = 6。你需要返回的结果为：
#
# [
#   [2, 4],
#   [2, 1, 3],
#   [3, 1, 2],
#   [4, 2]
# ]
# 现在我们拓展到搜索任意起始节点以及任意终止节点的路径。这道题其实被稍稍简化了，即每个节点除了给定指向左右子节点的指针外，
# 还给定了指向父节点的指针。因此，这道题就可以抽象为从任意节点出发，可以往三个方向走（左右子节点和父节点）的 DFS 路径遍历。
# 此外，为了避免出现「回头」的可能性，我们在递归时需要知道当前节点是从哪搜索过来的，并且避免回头搜索。
class ParentTreeNode:

    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None


class Solution:
    # @param {ParentTreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum3(self, root, target):
        # Write your code here
        results = []
        self.dfs(root, target, results)
        return results

    def dfs(self, root, target, results):
        if root is None:
            return

        path = []
        pre = None
        self.findSum(root, pre, target, path, results)

        self.dfs(root.left, target, results)
        self.dfs(root.right, target, results)

    def findSum(self, root, pre, target, path, results):
        path.append(root.val)
        target -= root.val

        if target == 0:
            results.append(path[:])
        #开始往三个方向check，在检查三个方向为不为None以及之前check过没
        if root.parent not in [None, pre]:
            self.findSum(root.parent, root, target, path, results)

        if root.left not in [None, pre]:
            self.findSum(root.left, root, target, path, results)

        if root.right not in [None, pre]:
            self.findSum(root.right, root, target, path, results)

        path.pop()
