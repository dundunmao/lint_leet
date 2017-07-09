# -*- encoding: utf-8 -*-
#heap方法

import heapq
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return None
        if k == 0:
            return None
        if k == 1:
            return matrix[0][0]
        array = []
        result = []
        count = 1
        heapq.heappush(array, (matrix[0][0], 0, 0))
        while count <= k:
            pop = heapq.heappop(array)
            if pop[2] + 1 < len(matrix[0]) and (matrix[pop[1]][pop[2] + 1], pop[1], pop[2] + 1) not in array:
                heapq.heappush(array, (matrix[pop[1]][pop[2] + 1], pop[1], pop[2] + 1))
            if pop[1] + 1 < len(matrix) and (matrix[pop[1] + 1][pop[2]], pop[1] + 1, pop[2]) not in array:
                heapq.heappush(array, (matrix[pop[1] + 1][pop[2]], pop[1] + 1, pop[2]))
            count += 1
        return pop[0]
#二分法
class Solution1:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def __init__(self):
        self.num = 0
        self.exists = None
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        m = len(matrix[0])
        left = matrix[0][0]
        right = matrix[n-1][m-1]
        while left <= right:
            mid = (right+left)/2
            type = self.helper(mid,matrix)
            if type[1] and type[0] == k:
                return mid
            elif type[0] < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def helper(self, value, matrix):
        n = len(matrix)
        m = len(matrix[0])
        exists = False
        num = 0
        i = n - 1
        j = 0
        while i >= 0 and j < m:
            if matrix[i][j] == value:
                exists = True
            if matrix[i][j] <= value:
                num += i + 1
                j += 1
            else:
                i -= 1
        return (num,exists)



if __name__ == "__main__":


    A = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]
    k = 19

    s = Solution1()

    print s.kthSmallest(A,k)