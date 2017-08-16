
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
        if not root or root == A or root == B:
            return root
        left = self.lowestCommonAncestor(root.left, A, B)    #左子树有A,B的LCA
        right = self.lowestCommonAncestor(root.right, A, B)   #右子树有A,B的LCA
        if left and right:  #如果左右子树都有,说明A,B一边一个,那root就是交点
            return root
        elif left is not None:     #如果只有左子树有,LCA就是左子树的LCA,就是left
            return left
        elif right is not None:   #如果只有右子树有,LCA就是右子树的LCA,就是left
            return right
        else:
            return None

class Solution3(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        list1 = []
        list2 = []
        find1 = self.find_node(root, p, list1)
        find2 = self.find_node(root, q, list2 )
        if not find1 or not find2:
            return None
        i = 1
        if list1[0].val == list2[0].val:
            res = list1[0]
        else:
            return None
        length = min(len(list1),len(list2))
        while i < length:
            if list1[i].val != list2[i].val:
                return res
            else:
                res = list1[i]
                i += 1
        return res
    def find_node(self,root,node,path):
        if root == None or node == None:
            return False
        path.append(root)
        l = self.find_node(root.left, node, path)
        r = self.find_node(root.right, node, path)
        if root != node and not l and not r:
            path.remove(root)
            return False
        return True
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
    # P = TreeNode(1)
    # P.left = TreeNode(2)
    # P.left.left = TreeNode(4)
    # P.left.right = TreeNode(5)
    # P.left.right.left = TreeNode(6)
    # P.left.right.right = TreeNode(7)
    # P.left.right.right.right = TreeNode(8)
    # P.right = TreeNode(3)
    P = TreeNode(-1)
    P.left = TreeNode(0)
    P.left.left = TreeNode(-2)
    P.left.right = TreeNode(4)
    # P.left.right.left = TreeNode(6)
    P.left.left.left = TreeNode(8)
    # P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(3)
    A = P.left.left.left
    B = P.left
    s = Solution3()
    print s.lowestCommonAncestor(P, A, B)