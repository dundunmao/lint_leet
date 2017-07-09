# -*- encoding: utf-8 -*-

class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        S.sort()
        counter = 0
        for i in range(len(S)-1,-1,-1):
            if i>1:
                target = S[i]
                nums = S[:i]
                counter += self.twoSum2(nums, target)
        return counter



    def twoSum2(self, nums, target):
    # Write your code here
        nums.sort()
        i = 0
        j = len(nums)-1
        count = 0
        while i<j:
            if nums[i]+nums[j]>target:
                count+=(j-i)
                j-=1
            else:
                i+=1
        return count