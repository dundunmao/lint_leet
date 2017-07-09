# -*- encoding: utf-8 -*-
# 下面这个不行，因为没说是sorted的
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)
        le = len(nums)
        i = 1
        flag = nums[0]
        while i <= le:
            if nums[i] != flag:
                return nums[i]
            else:
                i += 1
                flag += 1
        return None
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
#答案: sum = （首项+末项）/2
class Solution_leet(object):
    def missingNumber(self, nums):
        s = sum(nums)
        le = len(nums)
        return (le * (le + 1)) / 2 - s