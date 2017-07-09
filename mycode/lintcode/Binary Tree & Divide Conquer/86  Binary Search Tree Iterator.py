# -*- encoding: utf-8 -*-
# 设计实现一个带有下列属性的二叉查找树的迭代器：
#
# 元素按照递增的顺序被访问（比如中序遍历）
# next()和hasNext()的询问操作要求均摊时间复杂度是O(1)
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 对于下列二叉查找树，使用迭代器进行中序遍历的结果为 [1, 6, 10, 11, 12]
#
#    10
#  /    \
# 1      11
#  \       \
#   6       12


# 任何一个iterrator提供三个部分的借口:
# 1:构造函数
# 2:有没有下一个点
# 3:把下一个点拿出来
# 这题用in order 背程序
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""

class BSTIterator:
    #@param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.curt = root

    #@return: True if there has next node, or false
    def hasNext(self):
        return self.curt is not None or len(self.stack) > 0

    #@return: return next node
    def next(self):
        while self.curt is not None:
            self.stack.append(self.curt)
            self.curt = self.curt.left

        self.curt = self.stack.pop()
        node = self.curt
        self.curt = self.curt.right
        return node