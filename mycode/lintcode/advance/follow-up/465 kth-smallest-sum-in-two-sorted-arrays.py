# -*- encoding: utf-8 -*-
# heap 方法
import heapq
class Solution:

    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if not A or not B:
            return 0
        import heapq
        n, m = len(A), len(B)
        queue = []
        for i in range(min(k, m)):
            heapq.heappush(queue, (A[0] + B[i], 0, i))
        for i in range(k):
            pop = heapq.heappop(queue)
            value, col, row = pop[0],pop[1], pop[2]
            if i == k-1:
                return value
            if col + 1 < n:
                heapq.heappush(queue, (A[col + 1] + B[row], col + 1, row))
        return heapq.heappop(queue)[0]


class Solution1:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if A is None and B is None:
            return None
        n = len(A)
        m = len(B)
        if n == 0 and m == 0:
            return None
        if n == 0:
            return B[k-1]
        if m == 0:
            return A[k-1]
        matrix = [[float('inf') for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = B[i]+A[j]
        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue,(matrix[0][0],0,0))
        for x in range(k):
            node = heapq.heappop(queue)
            value = node[0]
            row = node[1]
            column = node[2]
            if x == k-1:
                return value
            if column+1<n and (matrix[row][column+1],row,column+1) not in queue:
                heapq.heappush(queue,(matrix[row][column+1],row,column+1))
            if row+1<m and (matrix[row+1][column],row+1,column) not in queue:
                heapq.heappush(queue,(matrix[row+1][column],row+1,column))

if __name__ == "__main__":


    A = [1,7,11]
    B=[2,4,6]
    k = 8
    s = Solution()

    print s.kthSmallestSum(A,B,k)