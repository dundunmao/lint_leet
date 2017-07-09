# coding:utf-8
# 给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
        if target is None:
            return -1
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            medium = start + (end - start) / 2
            if nums[medium] < target:
                start = medium
            elif nums[medium] >= target:
                end = medium
        if target == nums[start]:
            return start
        elif target == nums[end]:
            return end
        else:
            return -1