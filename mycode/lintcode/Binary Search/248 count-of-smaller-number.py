# -*- encoding: utf-8 -*-
# 给定一个整数数组 （下标由 0 到 n-1，其中 n 表示数组的规模，数值范围由 0 到 10000），以及一个 查询列表。对于每一个查询，将会给你一个整数，请你返回该数组中小于给定整数的元素的数量。
#
#  注意事项
#
# 在做此题前，最好先完成 线段树的构造 and 线段树查询 II 这两道题目。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 对于数组 [1,2,7,8,5] ，查询 [1,8,5]，返回 [0,4,2]

# 方法1: Sort and binary search


class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that
             are smaller that the given integer
    """

    def countOfSmallerNumber(self, A, queries):
        # write your code here
        # edge case:
        if A is None or queries is None:
            return None
        if len(A) == 0:
            return [0] * len(queries)
        # initial
        A.sort()
        result = []
        # main part
        for i in range(0, len(queries)):
            index = self.find_index(A, queries[i])
            result.append(index)
        return result

    def find_index(self, A, num):
        if len(A) == 0 or A[-1] < q:
            return len(A)
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] < num:
                start = mid
            else:
                end = mid
        if A[start] >= num:
            return start
        elif A[end] >= num:
            return end
        else:
            return end + 1

# 方法2:Build Segment Tree and Search
class segmentTree():
    def __init__(self, start, end,count):
        self.start = start
        self.end = end
        self.count = count
        self.left = None
        self.right = None
class Solution2:
    def countOfSmallerNumber(self, A, queries):
        root = self.build(0,10000)
        ans = []
        result = 0
        for i in range(0,len(A)):
            self.modifySegmentTree(root, A[i],1)
        for i in range(len(queries)):
            result = 0
            if queries[i]>0:
                result = self.querySegmentTree(root,0,queries[i]-1)
            ans.append(result)
        return ans

    def build(self,start,end):
        if start > end:
            return None
        root = segmentTree(start, end, 0)
        if start != end:
            mid = start + (end-start)/2
            root.left = self.build(start,mid)
            root.right = self.build(mid+1,end)
        else:
            root.count = 0
        return root

    def modifySegmentTree(self,root, index, value):
        if root.start == index and root.end == index: # 找到了
            root.count +=value
            return
        #查找
        mid = (root.start+root.end)/2
        if root.start <= index and index <= mid:
            self.modifySegmentTree(root.left, index, value)
        if mid < index and index <= root.end:
            self.modifySegmentTree(root.right, index, value)
        # 更新
        root.count = root.left.count + root.right.count

    def querySegmentTree(self,root,start, end):
        if start == root.start and root.end == end:  #相等
            return root.count
        mid = (root.start + root.end) / 2
        leftcount = 0
        rightcount = 0
        # 左子树区
        if start <= mid:
            if mid<end:
                leftcount = self.querySegmentTree(root.left,start,mid)
            else:
                leftcount = self.querySegmentTree(root.left, start, end)
        # 右子数区
        if mid <end:
            if start <= mid:
                rightcount = self.querySegmentTree(root.right,mid+1,end)
            else:
                rightcount = self.querySegmentTree(root.right, start,end)
        return leftcount+rightcount


# 考虑有重复,考虑 A = []



if __name__ == "__main__":
    A = []
    queries = [65,50]
    s = Solution3()
    print s.countOfSmallerNumber( A, queries)