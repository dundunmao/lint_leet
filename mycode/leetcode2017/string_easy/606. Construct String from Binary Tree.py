# -*- encoding: utf-8 -*-
# You need to construct a string consists of parenthesis and integers from a binary tree
#  with the preorder 中左右 traversing way.
# Example 1: Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
#
# Output: "1(2(4))(3)"
#
# Explanation: Originallay it needs to be "1(2(4)())(3()())",
# but you need to omit all the unnecessary empty parenthesis pairs.
# And it will be "1(2(4))(3)".

# Example 2:
# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4
#
# Output: "1(2()(4))(3)"
#
# Explanation: Almost the same as the first example,
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# stack法
# 前序遍历先放stack里root，然后pop出来，压入右，压入左，然后再pop，再压入右左
# 下面的方法是如果stack的最后一位不在visited里，就往ans里加其实括号和val，这时并不pop。当visited里有时pop，同时加结束括号
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        stack = []
        stack.append(t)
        visited = set([]) #不放重复node
        ans = []
        while len(stack) != 0:
            node = stack[-1]
            if node in visited:  #如果底下的三个if都没让stack里新加node，说明这个分支到头了，这里在看stack的最后一位，就会是visited的，就开始pop
                stack.pop()
                ans.append(')')  #因为分支到头了，所以有右括号了
            else:
                visited.add(node)
                ans.append('(')
                ans.append(str(node.val))
                if node.left is None and node.right is not None:
                    ans.append('()')  #如果有右没有左，就必须加一个（）
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        result = ''.join(ans)
        return result[1:-1]
#recursive法
class Solution2(object):
    def tree2str(self, t):
        if t is None:
            return ''
        if t.left is None and t.right is None: #如果没是叶子，就返回val
            return str(t.val) + ''
        if t.right is None:      #如果无右孩子，就只考虑左孩子，就返回 val + （ 左孩子的所有）
            return str(t.val) +'(' + str(self.tree2str(t.left)) + ')'
                                #如果有右孩子，不管左孩子有没有，都返回 val+ （左孩子的所有）+（右孩子的所有），这里如果无左孩子，就是（）里啥也没有。
        return str(t.val) + '(' + str(self.tree2str(t.left)) + ')(' + str(self.tree2str(t.right)) + ")"
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
    # P.left.left = TreeNode(4)
    # P.left.right = TreeNode(5)
    # P.left.right.left = TreeNode(6)
    # P.left.right.right = TreeNode(7)
    # P.left.right.right.right = TreeNode(8)
    P.right = TreeNode(3)
    s = Solution2()
    print s.tree2str(P)
    # (1(2(4())(5(6())(7(8()))))(3()))
    # 1(2(4)(5(6)(7()(8))))(3)
    # 1(2(4)(5(6)(7()(8))))(3)