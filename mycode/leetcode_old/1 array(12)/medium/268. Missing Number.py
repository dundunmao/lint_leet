# -*- encoding: utf-8 -*-
# 题目: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# 例如 nums = [0, 1, 3] return 2
# 思路 从1-n的和是(首项加末项乘以项数除以2),所以用它减去sum.就得出差的那个数了.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)