# coding:utf-8
# 3级
# 题目:Given inorder(中序) and postorder(后序) traversal of a tree, construct the binary tree.(无duplicates)
# 思路:Inorder中序:左根右。Postorder后序，左右根。所以后序的最后一个数就是这个树的root,用它去中序里面找到root的index,再分出来左右子树
#     在post里,从后往前,最后一个数是root,倒数第二个是右子树的root,倒数第三个是再右子树的root

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())      #后序里找到root
        inorderIndex = inorder.index(root.val)   #中序里找到root的index

        root.right = self.buildTree(inorder[inorderIndex+1:], postorder)  #右子树,这里不断的pop出右子树的点,到了下面就只剩左子树的点了.
        root.left = self.buildTree(inorder[:inorderIndex], postorder)     #左子树

        return root

#     我自己的
# class Solution(object):
#     def buildTree(self, inorder, postorder):
#         root =
#         return root

    # def dividtoTwo(self,inorder, postorder):
    #     indexRoot = inorder.index(postorder[-1])
    #     left_inorder = inorder[:indexRoot]
    #     left_postorder = postorder[:indexRoot]
    #     right_inorder = inorder[indexRoot+1:]
    #     right_postorder = postorder[indexRoot:-1]
    #     return left_inorder,left_postorder,right_inorder,right_postorder




if __name__ == '__main__':
     #        TREE 1
     # Construct the following tree
     #          26
     #        /   \
     #      10     3
     #    /    \     \
    #  #  4      6      3
    # P = TreeNode(26)
    # P.left = TreeNode(10)
    # P.left.left = TreeNode(4)
    # P.left.right = TreeNode(6)
    # P.right = TreeNode(3)
    # P.right.right = TreeNode(3)
    inorder = [1,4,3,2,0,6,7,5]
    postorder = [1,3,4,0,7,5,6,2]
    s= Solution()
    print s.buildTree(inorder,postorder)