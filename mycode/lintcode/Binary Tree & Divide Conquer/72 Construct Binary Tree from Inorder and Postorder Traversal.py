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


# inorder   左根右
# postorder 左右根
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
        root.val = postorder[-1]  #左右根，根在最后
        index_root_inorder = inorder.index(root.val)  #找到根在inorder的位置

        #left

        left_inorder = inorder[:index_root_inorder]   #左一半的位置
        left_postorder = postorder[:index_root_inorder]  #inorder和postorder左一半的位置是一样的
        root.left = self.buildTree(left_inorder, left_postorder)  #对左一半进行建树


        #right

        right_inorder = inorder[index_root_inorder+1:]  #右一半
        right_postorder = postorder[index_root_inorder:-1]  # inorder和postorder右一半的位置差一个root
        root.right = self.buildTree(right_inorder, right_postorder)


        return root