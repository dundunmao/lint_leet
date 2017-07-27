# -*- encoding: utf-8 -*-
# Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance.
# We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.
# Input:
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4
# 题：这道题给我们了一些数组，每个数组都是有序的，让我们从不同的数组中各取一个数字，
# 使得这两个数字的差的绝对值最大，让我们求这个最大值。
class Solution(object):
    def maxIndexDiff(self, nums):
        ans = 0
        le = len(nums)
        mini = nums[0][0]
        maxi = nums[0][le-1]
        for i in range(1,le):
            ans = max(ans,max(abs(nums[i][le-1]) - mini),
                              abs(maxi - nums[i][0]))
            mini = min(mini,nums[i][0])
            maxi = max(maxi,nums[i][le - 1])

        return ans