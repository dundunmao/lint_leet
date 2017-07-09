# coding:utf-8
# 3级
# 题目:Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# 例如:nums = [-2, 0, 1, 3],target = 2.Return 2. Because there are two triplets which sums are less than 2:[-2, 0, 1][-2, 0, 3]

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSumSmaller(self, nums):
        nums.sort()
        if len(num) <= 2:
            return []

