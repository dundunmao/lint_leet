# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # edge case
        if len(nums) < 3:
            return sum(nums)
#         main part
        res = 0
        diff = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                sum_three = nums[i] + nums[j] + nums[k]
                if sum_three == target:
                    return sum_three
                if abs(sum_three - target) < diff:
                    res = sum_three
                    diff = abs(sum_three - target)
                if sum_three < target:
                    j += 1
                else:
                    k -= 1
        return res