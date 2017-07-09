# coding:utf-8
# 2.5级 同106
# 题目:Given inorder(中序) and preorder(前序) traversal of a tree, construct the binary tree.(无duplicates)
# 思路:Inorder中序:左根右。Preorder前序，根左右。所以前序的第一个数就是这个树的root,用它去中序里面找到root的index,再分出来左右子树
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
    def buildTree(self,preorder,inorder):
        if not inorder or not preorder:
            return None

        root = TreeNode(preorder[0])      #后序里找到root
        preorder.pop(0)
        inorderIndex = inorder.index(root.val)   #中序里找到root的index
        root.left = self.buildTree( preorder,inorder[:inorderIndex])     #左子树
        root.right = self.buildTree(preorder,inorder[inorderIndex+1:] )  #右子树,这里不断的pop出右子树的点,到了下面就只剩左子树的点了.
        return root

if __name__ == '__main__':
    inorder = [1,2,3,4]
    preorder = [2,1,3,4]
    s= Solution()
    print s.buildTree(preorder,inorder)
