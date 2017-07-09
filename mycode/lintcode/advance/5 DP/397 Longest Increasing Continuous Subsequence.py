# -*- encoding: utf-8 -*-
class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if A is None or len(A) == 0:
            return 0
        n = len(A)
        result = 1
        length = 1
        # from left to right
        for i in range(1,n):
            if A[i] > A[i-1]:
                length+=1
            else:
                length =1
            result = max(result, length)
        # from right to left
        length = 1
        for i in range(n-2, -1,-1):
            if A[i]>A[i+1]:
                length +=1
            else:
                length = 1
            result = max(result, length)
        return result