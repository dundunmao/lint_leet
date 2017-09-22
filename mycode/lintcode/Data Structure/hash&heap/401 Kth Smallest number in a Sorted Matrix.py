# -*- encoding: utf-8 -*-
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.

# 方法一，先把一列加进去，每次往右走

import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k > len(matrix ) *len(matrix[0]):
            return None
        q = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            heapq.heappush(q, (matrix[i][0] ,i ,0))
        count = 0
        while heapq:
            res, i, j = heapq.heappop(q)
            count += 1
            if count == k:
                return res
            else:
                if i < len(matrix) and j + 1 < len(matrix[0]):
                    heapq.heappush(q, (matrix[i][j+1], i, j+1))


# 方法二：以matrix[0][0]为第一层，每次把一层加进去。还得加一个hash保证每次加进去的不重复
import heapq
class Solution1(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k > len(matrix ) *len(matrix[0]):
            return None
        q = []
        heapq.heappush(q, (matrix[0][0] ,0 ,0))
        count = 0
        index = {}
        index[(0 ,0)] = True
        while True :
            size = len(q)
            for ele in range(size):
                count += 1
                res ,i ,j = heapq.heappop(q)
                if count == k:
                    return res
                if ( i +1 ,j) not in index and i+ 1 < len(matrix) and j < len(matrix[0]):
                    heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
                    index[(i + 1, j)] = True
                if (i, j + 1) not in index and i < len(matrix) and j + 1 < len(matrix[0]):
                    heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
                    index[(i, j + 1)] = True
