# coding:utf-8
#  Given a binary tree, find the length of the longest consecutive sequence path.
# The path could be start and end at any node in the tree
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
#     1
#    / \
#   2   0
#  /
# 3
# Return 4 // 0-1-2-3-4
# 路径不再有自上而下的限制，而是任意起始节点以及任意终止节点。这就意味着可能存在着一条倒 V 型的路径。处理这种情况我们仍然使用分治法，
# 在每次递归时返回两个长度，一个是以当前节点为起始节点的路径，另一个就是以当前节点为终止节点的路径。而在处理一个节点时，
# 我们除了像上一题中简单仅考虑以当前节点为起始节点或终止节点以外，还需要考虑倒 V 型路径的可能性。

# divide&conquer

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive2(self, root):
        # Write your code here
        max_len, _, _, = self.helper(root)
        return max_len

    def helper(self, root): #return的是any-any的lca，从root向下的lca(以当前节点为起始节点)，从root向上的lca(以当前节点为终止节点)
        if root is None:
            return 0, 0, 0

        left_len, left_down, left_up = self.helper(root.left)
        right_len, right_down, right_up = self.helper(root.right)

        down, up = 0, 0
        if root.left is not None and root.left.val + 1 == root.val:
            down = max(down, left_down + 1)

        if root.left is not None and root.left.val - 1 == root.val:
            up = max(up, left_up + 1)

        if root.right is not None and root.right.val + 1 == root.val:
            down = max(down, right_down + 1)

        if root.right is not None and root.right.val - 1 == root.val:
            up = max(up, right_up + 1)

        len = max(down + 1 + up, left_len, right_len)

        return len, down, up