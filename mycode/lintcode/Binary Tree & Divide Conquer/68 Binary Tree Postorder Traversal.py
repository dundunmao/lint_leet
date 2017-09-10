# -*- encoding: utf-8 -*-
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    #recursive
    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        result = []
        # normal case
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        result.extend(left)
        result.extend(right)
        result.append(root.val)
        return result
    # stack
    def postorderTraversal_1(self, root):
        result = []
        if root is None:
            return result
        pre = None
        cur = root
        stack = [cur]
        while stack:
            cur = stack[-1]
            if pre == None or pre.left == cur or pre.right == cur:
                if cur.left != None:
                    stack.append(cur.left)
                elif cur.right != None:
                    stack.append(cur.right)
            elif cur.left == pre:
                if cur.right != None:
                    stack.append(cur.right)
            else:
                result.append(cur.val)
                stack.pop()
            pre = cur
        return result

# 非常简单的方法
class Solution3(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []
        pre = None
        cur = root
        res = []
        stack = [cur]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        res.reverse()
        return res
if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /   \
    #      2     3
    #    /   \   / \
    #  4      5  6  7

    P = TreeNode(1)
    P.left = TreeNode(2)
    P.left.left = TreeNode(4)
    P.left.right = TreeNode(5)
    # P.left.right.left = TreeNode(6)
    # P.left.right.right = TreeNode(7)
    # P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(3)
    P.right.left = TreeNode(6)
    P.right.right = TreeNode(7)
    #
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution3()
    print s.postorderTraversal(P)


