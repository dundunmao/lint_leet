
# coding:utf-8

# 给定一棵二叉树，找到两个节点的最近公共父节点(LCA)。
#
# 最近公共祖先是两个节点的公共的祖先节点且具有最大深度。
#
#  注意事项
#
# 假设给出的两个节点都在树中存在
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 对于下面这棵二叉树
#
#   4
#  / \
# 3   7
#    / \
#   5   6
# LCA(3, 5) = 4
#
# LCA(5, 6) = 7
#
# LCA(6, 7) = 7
# 分别列出:
# 左子树有A,B的LCA
# 右子树有A,B的LCA
# 如果左右子树都有,说明A,B一边一个,那root就是交点
# 如果只有左子树有,LCA就是左子树的LCA,就是left
# 如果只有右子树有,LCA就是右子树的LCA,就是left



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if root is None:
            return None
        if root is A or root is B:
            return root
        if root is not A and root is not B and root.left is None and root.right is None:
            return None

        left = self.lowestCommonAncestor(root.left, A, B)    #左子树有A,B的LCA
        right = self.lowestCommonAncestor(root.right, A, B)   #右子树有A,B的LCA
        if left is not None and right is not None:  #如果左右子树都有,说明A,B一边一个,那root就是交点
            return root
        elif left is not None:     #如果只有左子树有,LCA就是左子树的LCA,就是left
            return left
        elif right is not None:   #如果只有右子树有,LCA就是右子树的LCA,就是left
            return right
        else:
            return None
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

    A = P.left
    B = P.right.right
    s = Solution()
    print s.lowestCommonAncestor(P, A, B)