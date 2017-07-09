# -*- encoding: utf-8 -*-
# 满足三点:
# 1:左右都是full
# 2:左边min > 右边 max
# 3: 左边max 与 右边min 的差 小于等于1
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root, the root of binary tree.
    @return true if it is a complete binary tree, or false.
    """
    def isComplete(self, root):
        # Write your code here
        validate, max, min= self.helper(root)
        return validate
    def helper(self,root):
        if root is None:
            return True, 0,0
        left = self.helper(root.left)
        right = self.helper(root.right)
        if not left[0] or not right[0]:
            return False, 0,0
        if left[2]<right[1] or left[1]>right[2]+1:
            return False, 0,0
        return True, left[1]+1, right[2]+1

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
    # P.left.right.left = TreeNode(6)
    # P.left.right.right = TreeNode(7)
    # P.left.right.right.right = TreeNode(8)
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
    print s.isComplete(P)