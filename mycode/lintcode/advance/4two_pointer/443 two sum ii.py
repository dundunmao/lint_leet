
# -*- encoding: utf-8 -*-

class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        # Write your code here
        nums.sort()
        i = 0
        j = len(nums)-1
        count = 0
        while i<j:
            if nums[i]+nums[j]>target:
                count+=(j-i)    #当i,j符合条件时,j固定,i到j之间的数都符合条件
                j-=1
            else:
                i+=1
        return count