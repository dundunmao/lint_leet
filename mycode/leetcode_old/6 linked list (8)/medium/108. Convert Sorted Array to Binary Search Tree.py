class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, num):
        # write your code here
        if num is None:
            return None
        return self.build_tree(num, 0, len(num)-1)
    def build_tree(self, num, start, end):
        if start > end:
            return None
        node = TreeNode(num[(start+end)/2])
        node.left = self.build_tree(num, start, (start+end)/2-1)
        node.right = self.build_tree(num, (start+end)/2+1, end)
        return node