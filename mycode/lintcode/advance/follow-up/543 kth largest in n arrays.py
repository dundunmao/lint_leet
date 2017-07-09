# -*- encoding: utf-8 -*-
#heap方法

import heapq

class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        queue = []
        heapq.heapify(queue)
        for i, array in enumerate(arrays):
            from_id = i
            index = len(array) - 1
            array.sort()
            if index >= 0:
                value = arrays[i][index]
                heapq.heappush(queue,(-value, from_id, index))
        for i in xrange(k):
            node = heapq.heappop(queue)
            value = node[0]
            from_id = node[1]
            index = node[2]
            if i == k-1:
                return -value
            if index:
                index -= 1
                value = arrays[from_id][index]
                heapq.heappush(queue, (-value, from_id, index))

if __name__ == "__main__":


    # A = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]
    # k = 19
    A = [[9,3,2,4,8],[1,2,3,4,2]]
    k = 2
    s = Solution()

    print s.KthInArrays(A,k)