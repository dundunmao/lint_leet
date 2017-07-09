# coding:utf-8

# 给出一棵二叉树,返回其中序遍历
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出二叉树 {1,#,2,3},
#
#    1
#     \
#      2
#     /
#    3
# 返回 [1,3,2].
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        stack = []
        result = []
        cur = root
        while cur is not None or len(stack) !=0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result

class Solution2:
    def inorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result

class Solution3:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        stack = [root]
        while stack != []:
            node = stack[-1]
            while node.left:
                stack.append(node.left)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
        return result


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
    #
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution()
    print s.inorderTraversal(P)