# coding:utf-8

# 根据中序遍历和后序遍历树构造二叉树
#
#  注意事项
#
# 你可以假设树中不存在相同数值的节点
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出树的中序遍历： [1,2,3] 和后序遍历： [1,3,2]
#
# 返回如下的树：
#
#   2
#
#  /  \
#
# 1    3
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param inorder : A list of integers that inorder traversal of a tree
    @param postorder : A list of integers that postorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if inorder == []:
            return None
        root = TreeNode(postorder[-1])
        root.val = postorder[-1]
        index_root_inorder = inorder.index(root.val)

        #left

        left_inorder = inorder[:index_root_inorder]
        left_postorder = postorder[:index_root_inorder]
        root.left = self.buildTree(left_inorder, left_postorder)


        #right

        right_inorder = inorder[index_root_inorder+1:]
        right_postorder = postorder[index_root_inorder:-1]
        root.right = self.buildTree(right_inorder, right_postorder)


        return root