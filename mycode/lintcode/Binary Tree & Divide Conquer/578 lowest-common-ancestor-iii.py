# coding:utf-8
#  给一棵二叉树和二叉树中的两个节点，找到这两个节点的最近公共祖先LCA。
# 两个节点的最近公共祖先，是指两个节点的所有父亲节点中（包括这两个节点），离这两个节点最近的公共的节点。
# 返回 null 如果两个节点在这棵树上不存在最近公共祖先的话。
# 这题跟1的区别是1是 A,B一定存在树上，这题是不一定。
#
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
        res = self.helper(root, A, B)
        if res[1] and res[2]:
            return res[0]
        return None
    def helper(self, root, A, B): #return [LCA,find_A,find_B]
        if root is None:
            return [None, False, False]
        l = self.helper(root.left, A, B)
        r = self.helper(root.right, A, B)
        find_A = l[1] or r[1] or root == A #找到A的可能性是要么在左子树，要么在右子树，要么root就是A
        find_B = l[2] or r[2] or root == B #同理
        if A == root or B == root: #如果A或B是root，LCA=root，就返回【root,True,True】
            return [root, find_A, find_B]
        if l[0] != None and r[0] != None: #如果左右子树都存在LCA，说明root就是LCA
            return [root, find_A, find_B]
        if l[0] != None:     #如果左子树存在LCA，
            return [l[0], find_A, find_B]
        if r[0] != None:     #如果左子树存在LCA，
            return [r[0], find_A, find_B]
        return [None, find_A, find_B]
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
    # P = TreeNode(-1)
    # P.left = TreeNode(0)
    # P.left.left = TreeNode(-2)
    # P.left.right = TreeNode(4)
    # # P.left.right.left = TreeNode(6)
    # P.left.left.left = TreeNode(8)
    # # P.left.right.right.right = TreeNode(8)
    # P.right = TreeNode(3)
    A = P.left.right.right
    B = P.right
    s = Solution()
    print s.lowestCommonAncestor(P, A, B)