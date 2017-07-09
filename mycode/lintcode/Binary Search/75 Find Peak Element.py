# coding:utf-8
# 你给出一个整数数组(size为n)，其具有以下特点：
#
# 相邻位置的数字是不同的
# A[0] < A[1] 并且 A[n - 2] > A[n - 1]
# 假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。
#
#  注意事项
#
# 数组可能包含多个峰值，只需找到其中的任何一个即可
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组[1, 2, 1, 3, 4, 5, 7, 6]返回1, 即数值 2 所在位置, 或者6, 即数值 7 所在位置.


class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        l = len(A)
        if A is None or l == 0:
            return None
        start = 0
        end = l - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] > A[mid + 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
        if A[start] > A[end]:
            return start
        else:
            return end
if __name__ == "__main__":
    x = [1,1, 2, 1,1]
    s = Solution()
    print s.findPeak(x)