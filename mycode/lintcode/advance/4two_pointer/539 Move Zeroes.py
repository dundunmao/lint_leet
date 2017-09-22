# -*- encoding: utf-8 -*-

# 下面是答案，关键在于用不着管j位置是不是0
class Solution_daan(object):
    def moveZeroes(self, nums):
        i = 0
        for j in range(0 ,len(nums)):
            if nums[j] !=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
#  这个方法跟上一个不同的是，上一个j 觅食是找"不为0"的，这个判断 j "为0"，这个代码量大
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                if i == 0:
                    i = j + 1
                while i < len(nums):
                    if nums[i] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    else:
                        i += 1
                i += 1