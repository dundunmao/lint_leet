# coding:utf-8

# 给一个升序的数组，以及一个target，找到它在数组中出现的次数。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 [1, 3, 3, 4, 5] target = 3, 返回 2.
#
# 给出 [2, 2, 3, 4, 6] target = 4, 返回 1.
#
# 给出 [1, 2, 3, 4, 5] target = 6, 返回 0.
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def totalOccurrence(self, A, target):
        # Write your code here
        # edge case
        if A is None or len(A) == 0:
            return 0
        # initial
        first = 0
        last = 0
        start = 0
        end = len(A)-1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid]< target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            first = start
        elif A[end] == target:
            first = end
        else:
            return 0

        start = 0
        end = len(A)-1
        while start + 1 < end:
            mid = start + (end - start)/2
            if A[mid]<= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            last = end
        elif A[start] == target:
            last = start
        else:
            return 0
        return last - first + 1

