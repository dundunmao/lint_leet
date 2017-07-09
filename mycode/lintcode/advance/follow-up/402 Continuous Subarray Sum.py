# -*- encoding: utf-8 -*-
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        result = [0, 0]
        n = len(A)
        start = 0
        end = 0
        sum = 0
        ans = float('-inf')
        for i in range(0,n):
            if sum < 0:
                sum = A[i]
                start = i
                end = i
            else:
                sum += A[i]
                end = i
            if sum >= ans:
                ans = sum
                result = [start,end]
        return result


class Solution1:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        result = [0, 0]
        n = len(A)
        start = 0
        end = 0
        sum = [0 for i in range(n+1)]
        ans = float('-inf')
        for i in range(1,n+1):
            sum[i] = sum[i-1]+A[i-1]
            mini = float('inf')
            for j in range(0,i):
                if sum[j]<mini:
                    mini= sum[j]
                    start = j
            diff = sum[i] - mini
            if diff > ans:
                ans = diff
                end = i-1
                result = [start, end]
        return result
if __name__ == "__main__":
    s = Solution1()
    A = [-3,1,3,-3,4]
    print s.continuousSubarraySum(A)
