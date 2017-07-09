# coding:utf-8
# 在一个排好序的数组 A 中找到 i 使得 A[i] 最接近 target
#
#  注意事项
#
# There can be duplicate elements in the array, and we can return any of the indices with same value.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# [1, 2, 3] target = 2, 返回 1.
# [1, 4, 6] target = 3, 返回 1.
# [1, 4, 6] target = 5, 返回 1 或者 2.
# [1, 3, 3, 4] target = 2, 返回 0 或者 1 或者 2.

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        # Write your code here
        if A is None or len(A) == 0 or target is None:
            return -1
        start = 0
        end = len(A)-1
        while start+1 < end:
            mid = start + (end - start)/2
            if A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                return mid
        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        elif abs(A[end]-target) <= abs(A[start] - target):
            return end
        else: return start