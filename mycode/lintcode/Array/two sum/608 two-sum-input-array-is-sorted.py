# -*- encoding: utf-8 -*-
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
#  注意事项
#
# You may assume that each input would have exactly one solution.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# Given nums = [2, 7, 11, 15], target = 9
# return [1, 2]
# 用对冲指针
class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # Write your code here
        if nums is None or len(nums) == 0:
            return None
        le = len(nums)
        i = 0
        j = le - 1
        while i <= j:
            if nums[i] + nums[j] == target:
                return [i+1	,j+1]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1

        return None