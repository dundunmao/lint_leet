# coding:utf-8
# 给出一棵二叉树，返回其节点值的前序遍历。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一棵二叉树 {1,#,2,3},
#
#    1
#     \
#      2
#     /
#    3
#  返回 [1,2,3].

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# 方法一,non recursive,用stack
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = [root]
        result = []
        while stack != []:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # traverse
class Solution1:
    def preorderTraversal(self, root):
        result = []
        self.traverse(root,result)
        return result
    def traverse(self, root, result):
        if root is None:
            return
        result.append(root.val)
        self.traverse(root.left,result)
        self.traverse(root.right, result)

# divide and conquer
class Solution2:
    def preorderTraversal(self, root):
        result = []
        if root is None:
            return result
        result.append(root.val)
        result.extend(self.preorderTraversal(root.left))
        result.extend(self.preorderTraversal(root.right))
        return result