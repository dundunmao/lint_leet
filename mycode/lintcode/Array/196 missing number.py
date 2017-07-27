# -*- encoding: utf-8 -*-
# 方法一
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)+1):
            if i == len(nums):
                return i
            elif i != nums[i]:
                return i
# 所以用hash
class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for i in range(len(nums)+1):
            hash[i] = True
        for i in range(len(nums)):
            if hash.has_key(nums[i]):
                hash[nums[i]] = False
        for key,value in hash.items():
            if value == True:
                return key
# 方法三
#答案: sum = （首项+末项）/2
class Solution_leet(object):
    def missingNumber(self, nums):
        s = sum(nums)
        le = len(nums)
        return (le * (le + 1)) / 2 - s