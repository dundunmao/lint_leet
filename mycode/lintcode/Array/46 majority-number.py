# -*- encoding: utf-8 -*-
#用hash
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le = len(nums)
        hash = {}
        for num in nums:
            if hash.has_key(num):
                hash[num] += 1
                if hash[num] > le / 2:
                    return num
            else:
                hash[num] = 1
                if hash[num] > le / 2:
                    return num
