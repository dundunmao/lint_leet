# -*- encoding: utf-8 -*-
class Solution:
    # @param {int[]} A an integer array
    # @param {int} start an integer
    # @param {int} end an integer
    # @return {int} the number of possible answer
    def subarraySumII(self, A, start, end):
        n = len(A)
        for i in range(1,n):
            A[i] += A[i-1]
        A.sort()
        count = 0
        for i in range(0, n):
            if A[i] >= start and A[i] <= end:
                count += 1
            l = A[i] - end
            r = A[i] - start
            count += self.helper(A, n, r+1) - self.helper(A, n, l)
        return count
    def helper(self, A, n, value):
        if A[n-1] < value:
            return n
        l = 0
        r = n - 1
        ans = 0
        while l <= r:
            mid = (l+r)/2
            if value <= A[mid]:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans        # Write your code here
if __name__ == "__main__":
    s = Solution()
    A = [1,2,3,4]
    s = 1
    e = 3
    print s.subarraySumII(A,s,e)