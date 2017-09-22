# coding:utf-8
# 对于一个有n个数的整数数组，在对应的线段树中, 根节点所代表的区间为0-n-1, 每个节点有一个额外的属性max，值为该节点所代表的数组区间start到end内的最大值。
#
# 为SegmentTree设计一个 query 的方法，接受3个参数root, start和end，线段树root所代表的数组中子区间[start, end]内的最大值。

# 样例
# 对于数组 [1, 4, 2, 3], 对应的线段树为：
#
#                   [0, 3, max=4]
#                  /             \
#           [0,1,max=4]        [2,3,max=3]
#           /         \        /         \
#    [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
# query(root, 1, 1), return 4
#
# query(root, 1, 2), return 4
#
# query(root, 2, 3), return 3
#
# query(root, 0, 2), return 4

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if start > end or root is None:
            return 0
        if start <= root.start and end >= root.end:
            return root.max
        mid = (root.start + root.end)/2
        left_max = float('-inf')
        right_max = float('-inf')
        # 左区间
        if start <= mid:
            if mid < end: #分裂
                left_max = self.query(root.left, start, mid)
            else:   #包含
                left_max = self.query(root.left, start, end)
        #右区间
        if mid < end:
            if start <= mid:
                right_max = self.query(root.right, mid + 1, end)
            else:
                right_max = self.query(root.right, start, end)
        # else 就是不相交
        return max(left_max, right_max)