# Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.
#
# The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.
#
# Example 1:
# Input:
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
#
# v = 1
#
# d = 2
#
# Output:
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     /
#  3   1   5
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from Queue import Queue

#leetcode方法
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        q = self.bfs(root, d - 1)
        size = q.qsize()
        while size>0:
            node = q.get()
            if node.left:
                temp = node.left
                new_node = TreeNode(v)
                node.left = new_node
                new_node.left = temp
            else:
                new_node = TreeNode(v)
                node.left = new_node
            if node.right:
                temp = node.right
                new_node = TreeNode(v)
                node.right = new_node
                new_node.right = temp
            else:
                new_node = TreeNode(v)
                node.right = new_node
            size -= 1
        return root

    def bfs(self, root, depth):
        j = 1
        q = Queue()
        q.put(root)
        while j != depth:
            le = q.qsize()
            for i in range(le):
                nod = q.get()
                if nod.left is not None:
                    q.put(nod.left)
                if nod.right is not None:
                    q.put(nod.right)
            j += 1
        return q
#自己方法
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            x = TreeNode(v)
            x.left = root
            return x
        queue = [root]
        for _ in range(d-2):
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        for node in queue:
            l = TreeNode(v)
            l.left = node.left
            node.left = l
            r = TreeNode(v)
            r.right = node.right
            node.right = r
        return root
if __name__ == "__main__":
#      4
#    /  \
#  6
# /  \
#3   1

    P = TreeNode(4)
    P.left = TreeNode(6)
    P.left.left = TreeNode(3)
    P.left.right = TreeNode(1)
    # P.right = TreeNode(2)
    # P.right.left = TreeNode(5)
    v = 1
    d = 3
    s = Solution()
    print s.addOneRow(P,v,d)