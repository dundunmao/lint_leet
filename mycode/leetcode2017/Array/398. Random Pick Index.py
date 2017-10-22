# -*- encoding: utf-8 -*-
# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
#
# Example:
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
# 给一个数组里面有duplicate，给你个数，返回这个数的任意一个index
# 属于Reservoir Sampling问题
import random
class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.rnd = random

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = -1
        count = 0
        for i in range(0,len(self.nums)):
            if self.nums[i] != target:
                continue
            count += 1
            if self.rnd.choice(count) == 0:
                res = i
        return res




        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)