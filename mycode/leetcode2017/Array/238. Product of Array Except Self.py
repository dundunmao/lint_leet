# -*- encoding: utf-8 -*-
# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
# 这要考虑有0的情况，有一个0和多个0还不一样，
#     还有考虑有-的情况

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for i in range(n)]
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(n-1,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res

class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = float('inf')
        for i in nums:
            if nums[i] == 0:
                if index == float('inf'):
                    index = 0
                else:
                    return [0]*len(nums)
        if index != float('inf'):
            mult = 1
            for i in range(len(nums)):
                if i != index:
                    mult *= nums[i]
            for i in range(len(nums)):
                if i != index:
                    nums[i] = 0
                else:
                    nums[i] = mult
            return nums
        else:
            mult = 1
            for ele in nums:
                mult = mult*ele
            for i in range(len(nums)):
                nums[i] = mult/nums[i]
            return nums