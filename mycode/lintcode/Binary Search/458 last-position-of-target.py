# coding:utf-8
# 给一个升序数组，找到target最后一次出现的位置，如果没出现过返回-1
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 [1, 2, 2, 4, 5, 5].
#
# target = 2, 返回 2.
#
# target = 5, 返回 5.
#
# target = 6, 返回 -1.
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if A is None or len(A) == 0 or target is None:
            return -1
        start = 0
        end = len(A)-1
        while start+1 < end:
            mid = start + (end - start)/2
            if A[mid] <= target:
                start = mid
            elif A[mid] > target:
                end = mid
        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        else:
            return -1
            