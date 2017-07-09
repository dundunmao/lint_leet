# -*- encoding: utf-8 -*-
# 给定一个二叉树，判断它是否是合法的二叉查找树(BST)
#
# 一棵BST定义为：
#
# 节点的左子树中的值要严格小于该节点的值。
# 节点的右子树中的值要严格大于该节点的值。
# 左右子树也必须是二叉查找树。
# 一个节点的树也是二叉查找树。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 一个例子：
#
#   2
#  / \
# 1   4
#    / \
#   3   5
# 上述这棵二叉树序列化为 {2,1,4,#,#,3,5}.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        validate, _, _ =  self.helper(root)
        return validate

    def helper(self, root):
        if root is None:
            return True, float('-inf'), float('inf')
        validate_left, max_val_left, min_val_left  = self.helper(root.left)
        validate_right, max_val_right, min_val_right = self.helper(root.right)


        if validate_left is False:
            return False, 0, 0
        elif max_val_left >= root.val:
            return False, 0, 0

        if validate_right is False:
            return False, 0, 0
        elif min_val_right <= root.val:
            return False, 0, 0

        return True, max(root.val, max_val_right), min(root.val, min_val_left)

class Solution1:
    def isValidBST(self, root):
        validate, maxi, mini = self.helper(root)
        return validate

    def helper(self, root):
        if root is None:
            return True, float('-inf'), float('inf')
        left = self.helper(root.left)
        if not left[0] or left[1] >= root.val:
            return False, 0, 0
        right = self.helper(root.right)
        if not right[0] or right[2] <= root.val:
            return False, 0, 0
        return True, max(root.val, right[1]), min(root.val, left[2])

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
    # Q = P.left.right

    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution1()
    print s.isValidBST(P)
