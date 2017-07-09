# coding:utf-8
# 将 k 个排序数组合并为一个大的排序数组。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出下面的 3 个排序数组：
#
# [
#   [1, 3, 5, 7],
#   [2, 4, 6],
#   [0, 8, 9, 10, 11]
# ]
# 合并后的大数组应为：
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
from heapq import *
class Solution:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        # Write your code here
        result = []
        length = max([len(item) for item in arrays])
        for i in range(0,length):
            for array in arrays:
                if len(array)>0:
                    heappush(result,heappop(array))
        return sorted(result)


class Solution1:
    # @param {int[][]} arrays k sorted integer arrays
    # @return {int[]} a sorted array
    def mergekSortedArrays(self, arrays):
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heappush(heap, (array[0], index, 0))

        while len(heap):
            val, item, id = heap[0]
            heappop(heap)
            result.append(val)
            if id + 1 < len(arrays[item]):
                heappush(heap, (arrays[item][id + 1], item, id + 1))
        return result
if __name__ == '__main__':
    arrays = [[1,3,5,7],[2,4,6],[0,8,9,10,11]]
    s = Solution1()
    print s.mergekSortedArrays(arrays)