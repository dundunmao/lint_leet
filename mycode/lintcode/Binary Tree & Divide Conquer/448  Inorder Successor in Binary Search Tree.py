# -*- encoding: utf-8 -*-
# 给一个二叉查找树(什么是二叉查找树)，以及一个节点，求该节点的中序遍历后继，如果没有返回null
#  注意事项
# It's guaranteed p is one node in the given tree.
# 样例
# 给出 tree = [2,1] node = 1:
#
#   2
#  /
# 1
# 返回 node 2.
#
# 给出 tree = [2,1,3] node = 2:
#
#   2
#  / \
# 1   3
# 返回 node 3.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 找到bst里某一个node的inorder的下一个node。就是求这个node右子树的最左点,如果没有右子树,就是他上一层的root
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        last_root = None
        while root != None and root.val != p.val:
            if root.val > p.val:
                last_root = root   #只有往左子树走的时候,才把这个root记录着(因为当某个点无右子树时,他的下一个点是他的上一层,就是这个root),把左子树都走完了前一直是这个root
                root = root.left
            else:
                root = root.right
        #遍历到最底层还没找到
        if root is None:
            return None
         #找到了，这个node右子树空，那他的下一个点就是他上层那个root
        if root.right is None:
            if last_root:
                return last_root.val
            else:
                return None
         #如果有右子树，要找这个右子树的最小点
        root = root.right
        while root.left != None:
            root = root.left
        return root.val


if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          5
    #        /   \
    #      3     6
    #    /   \
    #  2      4

    P = TreeNode(5)
    P.left = TreeNode(3)
    P.left.left = TreeNode(2)
    P.left.right = TreeNode(4)
    P.right = TreeNode(6)
    Q = P.left.right
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution()
    print s.inorderSuccessor(P,Q)
