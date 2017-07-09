# -*- encoding: utf-8 -*-
class Solution:
    # @param {int[]} A an integer array
    # @param {int} start an integer
    # @param {int} end an integer
    # @return {int} the number of possible answer
    def subarraySumII(self, A, start, end):
        n = len(A)
        sum = [0 for i in range(n+1)]
        count = 0
        for i in range(0, n+1):
            sum[i] = sum[i-1]+A[i-1]
            count += self.helper(sum, i-1, sum[i]-start+1) - self.helper(sum, i-1, sum[i]-end)
        return count
    def helper(self, A, last, value): #二分法找到value位置,算出比value小的值有多少个
        if A[0] >= value:
            return 0
        if A[last] < value:
            return last + 1
        l = 0
        r = last
        while l+1 < r:
            mid = (l+r)/2
            if A[mid] < value:
                l = mid
            else:
                r = mid - 1
        if A[r] < value:
            return r + 1
        return l + 1
if __name__ == "__main__":
    s = Solution()
    A = [1, 2, 3, 4]
    st = 1
    ed = 3
    print s.subarraySumII(A,st,ed)

