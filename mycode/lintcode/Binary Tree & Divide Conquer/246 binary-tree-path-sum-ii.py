
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
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1(object):
    def __init__(self):
        self.res = 0
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        path = []
        self.helper(root, target, path)
        return self.res

    def helper(self, root, target, path):
        if root is None:
            return
        path.append(root.val)
        self.sum_num(path,target)
        self.helper(root.left, target, path)
        self.helper(root.right, target, path)
        path.pop()

    def sum_num(self, path, target):
        tmp = target
        l = len(path)-1
        for i in xrange(l , -1, -1):
            tmp -= path[i]
            if tmp == 0:
                self.res+=1

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0

        root_l = self.pathSum(root.left, target-root.val)
        root_r = self.pathSum(root.right, target - root.val)
        l = self.pathSum(root.left, target)
        r = self.pathSum(root.right, target)
        return root_l+root_r+l+r



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

    s = Solution()
    print s.pathSum(P,t)
