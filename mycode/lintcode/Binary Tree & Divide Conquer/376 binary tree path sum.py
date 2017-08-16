# coding:utf-8
# Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
# A valid path is from root node to any of the leaf nodes.
# Have you met this question in a real interview? Yes
# Example:
# Given a binary tree, and target = 5:
#
#      1
#     / \
#    2   4
#   / \
#  2   3
#
#  return
#
# [
#   [1, 2, 2],
#   [1, 4]
# ]

#往path里加数,先尝试,在还原.
# 注意题意是从root --> leaf
# 当target为0时,说明正好减完,这时往result里加

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        if root is None:
            return []
        result = []
        path = []
        path.append(root.val)
        self.helper(root,target-root.val,path,result)
        return result

    def helper(self,root,target,path,result):
        # if root is None:
        #     return
        if root.left is None and root.right is None:
            if target == 0:
                # array = [i for i in path]
                # result.append(array)
                result.append(path[:])  #path[:]是创建了一个硬拷贝，跟上面一个效果
            return
        #尝试往左走,尝试完要还原
        if root.left:
            path.append(root.left.val)   #尝试
            self.helper(root.left, target-root.left.val, path,result)
            path.pop()                   #还原
        #尝试往右走,尝试完要还原
        if root.right:
            path.append(root.right.val)
            self.helper(root.right, target-root.right.val,path,result)
            path.pop()

class Solution1:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        result = []
        path = []
        self.dfs(root, path, result, 0,  target)

        return result

    def dfs(self, root, path, result, len, target):
        if root is None:
            return
        path.append(root.val)
        len += root.val

        if root.left is None and root.right is None and len == target:
            result.append(path[:])

        self.dfs(root.left, path, result, len, target)
        self.dfs(root.right, path, result, len, target)

        path.pop()
if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          5
    #        /   \
    #      3     6
    #    /   \
    #  2      4

    P = TreeNode(1)
    P.left = TreeNode(2)
    P.left.left = TreeNode(3)
    P.left.right = TreeNode(4)
    P.right = TreeNode(5)
    Q = P.left.right
    t = 6
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution()
    print s.binaryTreePathSum(P,t)
