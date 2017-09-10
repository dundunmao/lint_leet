# coding:utf-8
#  给一棵二叉树，找出从根节点到叶子节点的所有路径。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出下面这棵二叉树：
#
#    1
#  /   \
# 2     3
#  \
#   5
# 所有根到叶子的路径为：
#
# [
#   "1->2->5",
#   "1->3"
# ]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
# traverse
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        if root is None:
            return []
        res = []
        path = []
        self.helper(root,path,res)
        return res
    def helper(self,root,path,res):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            ans = '->'.join([str(i) for i in path])
            res.append(ans)
        # if root.left:
        self.helper(root.left,path,res)
        # if root.right:
        self.helper(root.right,path,res)
        path.pop()
# 分治
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here\
        path = []
        if root is None:
            return path
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        for ele in left:
            path.append(str(root.val) + '->' + ele)
        for ele in right:
            path.append(str(root.val) + '->' + ele)
        if len(path) == 0:
            path.append('' + str(root.val))
        return path
# 我的分治，略微不同
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        l = self.binaryTreePaths(root.left)
        r = self.binaryTreePaths(root.right)
        for ele in l:
            ele.insert(0, root.val)
        for ele in r:
            ele.insert(0, root.val)
        return l + r


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

    s = Solution5()
    print s.binaryTreePaths(P)