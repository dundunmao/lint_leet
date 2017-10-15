# -*- encoding: utf-8 -*-
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1



# 1:从后找到递减的那一块a[i : ]
# 2: 在递减区间找第一个比a[i-1]大的数 a[j]
# 3:i-1和j swap
# 4: 最后把decrease变成increase
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >=0 and nums[i + 1] <= nums[i]:
            i -=1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j]<= nums[i]:
                j -=1
            nums[i],nums[j] = nums[j],nums[i]
        self.reverse_part(nums, i+1, len(nums)-1)

    def reverse_part(self,nums,i,j):
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
