# coding:utf-8
# 根据前序遍历和中序遍历树构造二叉树.
#
#  注意事项
#
# 你可以假设树中不存在相同数值的节点
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出中序遍历：[1,2,3]和前序遍历：[2,1,3]. 返回如下的树:
#
#   2
#  / \
# 1   3

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        if preorder == []:
            return None
        root = TreeNode(preorder[0])
        root.val = preorder[0]
        index_root_inorder = inorder.index(root.val)

        #left
        left_preorder = preorder[1:index_root_inorder+1]
        left_inorder = inorder[:index_root_inorder]
        root.left = self.buildTree(left_preorder, left_inorder)


        #right

        right_preorder = preorder[index_root_inorder+1:]
        right_inorder = inorder[index_root_inorder+1:]
        root.right = self.buildTree(right_preorder, right_inorder)


        return root