# -*- encoding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return
        le = len(nums)
        i = 0
        while i < len:
            while i < le and nums[i] != 0:
                i += 1
            j = i+1
            if j > len(nums) - 1:
                return
            while j < le and nums[j] == 0:
                j += 1
            if j > le - 1:
                return
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j += 1
# 下面是答案，关键在于用不着管j位置是不是0
class Solution_daan(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(0 ,len(nums)):
            if nums[i] !=0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1