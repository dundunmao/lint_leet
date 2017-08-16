# -*- encoding: utf-8 -*-
# 给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束（路径和为两个节点之间所在路径上的节点权值之和）
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一棵二叉树：
#
#        1
#       / \
#      2   3
# 返回 6
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 用resultTyoe这个class
class ResultType(object):
    def __init__(self, root2any, any2any):
        self.root2any = root2any
        self.any2any = any2any

class Solution1:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def helper(self, root):
        if root is None:
            return ResultType(float('-inf'), float('-inf'))

        # Divide
        left = self.helper(root.left)
        right = self.helper(root.right)

        # Conquer
        root2any = max(0,max(left.root2any, right.root2any)) + root.val

        any2any = max(left.any2any, right.any2any)
        any2any = max(any2any,
                      max(0,left.root2any) +
                      max(0,right.root2any) +
                      root.val)

        return ResultType(root2any, any2any)

    def maxPathSum(self, root):
        # write your code here
        result = self.helper(root)
        return result.any2any




# 不用resultTyoe这个class,这个方法最好

class Solution2:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        root2any, any2any = self.helper(root)
        return any2any

    def helper(self, root):
        if root is None:
            return (float('-inf'), float('-inf')) #考虑到最后一个node.val是负数,必须要取,所以要跟负无穷比较

        # Divide
        root2any_left, any2any_left = self.helper(root.left)
        root2any_right, any2any_right = self.helper(root.right)

        # Conquer
        root2any = max(0,root2any_left, root2any_right) + root.val  #如果左右子树小于0,那就只去root的值

        any2any = max(any2any_left,
                      any2any_right,
                      max(0,root2any_left) + max(0,root2any_right) + root.val) #也是如果是负数,就不取了
        return root2any, any2any




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
    s = Solution7()
    print s.maxPathSum(P)





