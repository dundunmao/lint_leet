# coding:utf-8
# 在一个排序数组中找一个数，返回该数出现的任意位置，如果不存在，返回-1
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组 [1, 2, 2, 4, 5, 5].
#
# 对于 target = 2, 返回 1 或者 2.
# 对于 target = 5, 返回 4 或者 5.
# 对于 target = 6, 返回 -1.
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
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
        else:
            return -1
if __name__ == "__main__":
    A = [1,2,7,8,5]
    target = 1
    s = Solution()
    print s.findPosition(A, target)