# coding:utf-8
# 线段树是一棵二叉树，他的每个节点包含了两个额外的属性start和end用于表示该节点所代表的区间。start和end都是整数，并按照如下的方式赋值:
#
# 根节点的 start 和 end 由 build 方法所给出。
# 对于节点 A 的左儿子，有 start=A.left, end=(A.left + A.right) / 2。
# 对于节点 A 的右儿子，有 start=(A.left + A.right) / 2 + 1, end=A.right。
# 如果 start 等于 end, 那么该节点是叶子节点，不再有左右儿子。
# 对于给定数组设计一个build方法，构造出线段树
# 样例
# 给出[3,2,1,4]，线段树将被这样构造
#
#                  [0,  3] (max = 4)
#                   /            \
#         [0,  1] (max = 3)     [2, 3]  (max = 4)
#         /        \               /             \
# [0, 0](max = 3)  [1, 1](max = 2)[2, 2](max = 1) [3, 3] (max = 4)

class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
class Solution:
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, A):
        start = 0
        end = len(A)-1
        return self.helper(start, end, A)
    def helper(self,start, end, A):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, A[start])
        if start == end:
            return root
        mid = (start + end)/2
        # 算出left和right的属性
        root.left = self.helper(start, mid, A)
        root.right = self.helper(mid+1, end, A)
        #这里再把max这个属性算出来
        if root.left != None and root.left.max > root.max:
            root.max = root.left.max
        if root.right != None and root.right.max > root.max:
            root.max = root.right.max  #如果有right，right的max就会更新left的max值
        return root