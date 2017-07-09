# -*- encoding: utf-8 -*-
#失败
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
from Queue import Queue
class Solution:
    """
    @param root, the root of binary tree.
    @return true if it is a mirror of itself, or false.
    """
    def isSymmetric(self, root):
        # Write your code here
        if root is None:
            return True
        q = Queue()
        q.put(root)
        while q.qsize()>0:
            len = q.qsize()
            array = []
            for i in range(len):
                node = q.get()
                if node.left:
                    array.append(node.left.val)
                    q.put(node.left)
                if node.right:
                    array.append(node.right.val)
                    q.put(node.right)
            if not self.isSy(array):
                return False
        return True

    def isSy(self,array):
        i = 0
        j = len(array)-1
        while i < j:
            if array[i]!=array[j]:
                return False
            i+=1
            j-=1
        return True

#答案
class Solution1:
    def isSymmetric(self, root):
        # Write your code here
        if root:
            return self.help(root.left, root.right)
        return True

    def help(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False




if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /    \
    #      2       2
    #    /   \   /  \
    #  3      4 4   3
    #
    P = TreeNode(1)
    P.left = TreeNode(2)
    P.right = TreeNode(2)
    P.left.left = TreeNode(3)
    P.left.right = TreeNode(4)
    P.right.left = TreeNode(4)
    P.right.right = TreeNode(3)
    # P.left.right.right.right = TreeNode(8)

    #
    #
    # Q = Node(26)
    # Q.left = Node(10)
    # Q.left.left = Node(4)
    # Q.left.right = Node(6)
    # Q.right = Node(3)
    # # Q.right.right = Node(3)

    s = Solution()
    s.isSymmetric(P)