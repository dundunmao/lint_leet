# -*- encoding: utf-8 -*-
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            hash[i + 1] = True
        for i in range(len(nums)):
            if hash.has_key(nums[i]):
                hash[nums[i]] = False
        result = []
        for key, value in hash.items():
            if value == True:
                result.append(key)
        return result
