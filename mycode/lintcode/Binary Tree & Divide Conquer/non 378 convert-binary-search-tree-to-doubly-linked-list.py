# coding:utf-8
#  将一个二叉查找树按照中序遍历转换成双向链表。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给定一个二叉查找树：
#
#     4
#    / \
#   2   5
#  / \
# 1   3
# 返回 1<->2<->3<->4<->5。
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.prev = next
class ResultType():
    def __init__(self,f = None,l = None):
        self.first = f
        self.last = l

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        if root is None:
            return None
        result = self.helper(root)
        return result.first
    def helper(self,root):
        if root is None:
            return None
        l = self.helper(root.left)
        r = self.helper(root.right)
        node = DoublyListNode(root.val)
        result = ResultType(None,None)
        if l == None:
            result.first = node
        else:
            result.first = l.first
            l.last.next = node
            node.prev = l.last
        if r == None:
            result.last = node
        else:
            result.last = r.last
            r.first.prev = node
            node.next = r.first
        return result

#或者不用ResultType
class Solution1:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        if root is None:
            return None
        result = self.helper(root)
        return result[0]
    def helper(self,root):
        if root is None:
            return None
        l = self.helper(root.left)
        r = self.helper(root.right)
        node = DoublyListNode(root.val)
        first = None
        last = None
        if l == None:
            first = node
        else:
            first = l[0]
            l[1].next = node
            node.prev = l[1]
        if r == None:
            last = node
        else:
            node.next = r[0]
            r[0].prev = node
            last = r[1]
        return [first,last]