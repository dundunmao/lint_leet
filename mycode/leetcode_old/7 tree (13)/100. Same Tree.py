# -*- encoding: utf-8 -*-
# 2级
# 标签：Tree Depth-first Search
# 题目；两个tree一样不
# 思路：递归
# 边界条件：如果两个都为空，就返回True。如果一个空一个不空返回False，如果都不空，值不一样就false
# 调用：两个的左子树一样，并且，两个的右子树一样

# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # Check fi the data of both roots is same and data of left and right subtrees are also same
        return (p.data == q.data and self.isSameTree(p.left , q.left)and self.isSameTree(p.right, q.right))


if __name__ == '__main__':
     #        TREE 1
     # Construct the following tree
     #          26
     #        /   \
     #      10     3
     #    /    \     \
     #  4      6      3
    P = Node(26)
    P.left = Node(10)
    P.left.left = Node(4)
    P.left.right = Node(6)
    P.right = Node(3)
    P.right.right = Node(3)

    Q = Node(26)
    Q.left = Node(10)
    Q.left.left = Node(4)
    Q.left.right = Node(6)
    Q.right = Node(3)
    # Q.right.right = Node(3)

    s = Solution()
    print s.isSameTree(P,Q)