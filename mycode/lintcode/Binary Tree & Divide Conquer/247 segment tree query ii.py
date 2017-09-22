# coding:utf-8
# 对于一个数组，我们可以对其建立一棵 线段树, 每个结点存储一个额外的值 count 来代表这个结点所指代的数组区间内的元素个数. (数组中并不一定每个位置上都有元素)
# 实现一个 query 的方法，该方法接受三个参数 root, start 和 end, 分别代表线段树的根节点和需要查询的区间，找到数组中在区间[start, end]内的元素个数。
# 对于数组 [0, 空，2, 3], 对应的线段树为：
#                      [0, 3, count=3]
#                      /             \
#           [0,1,count=1]             [2,3,count=2]
#           /         \               /            \
#    [0,0,count=1] [1,1,count=0] [2,2,count=1], [3,3,count=1]
# query(1, 1), return 0
# query(1, 2), return 1
# query(2, 3), return 2
# query(0, 2), return 2

# 解题：可以看出【0，0】【1，1】【2，2】【3，3】对应的是数组里的【0，空，2，3】这四个数。
# 如果线段包含了root的线段range，root的count就是结果
# if start <= root.start and root.end <= end:
#             return root.count
# 找root的mid，这个mid是其左右子树的分界线：
# 	•	如果start<=mid，说明左子树involve了，在左子树里找一共多少个count，
# 再看end在不在左子树里，就是end<mid，
# 如果是：left_count = self.query(root.left, start, mid)代表左子树里有多少个在start和mid之间
# 如果不是：left_count = self.query(root.left, start, end)代表左子树里有多少个在start和end之间
#  
# 	•	如果end>=mid，说明右子树involve了，在右子树里找一共多少个count，
# 再看start在不在右子树里，就是start>mid，
# 如果是：right_count = self.query(root.right, mid + 1, end)代表右子树里有多少个在mid和end之间
# 如果不是：right_count = self.query(root.right, start, end)代表右子树里有多少个在start和end之间
#  
# 最后把左右count加起来left_count + right_count

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
        if start <= root.start and root.end <= end:
            return root.count
        mid = (root.start + root.end)/2
        left_sum = 0
        right_sum = 0
        # 左区间
        if start <= mid:
            if mid < end: #分裂
                left_sum = self.query(root.left, start, mid)
            else:   #包含
                left_sum = self.query(root.left, start, end)
        #右区间
        if mid < end:
            if start <= mid:
                right_sum = self.query(root.right, mid + 1, end)
            else:
                right_sum = self.query(root.right, start, end)
        # else 就是不相交
        return left_sum + right_sum

if __name__ == "__main__":

    target = 8
    s = Solution2()
    print s.search(nums,target)