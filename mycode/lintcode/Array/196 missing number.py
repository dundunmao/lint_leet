# -*- encoding: utf-8 -*-
# 方法一：index 对应法
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n not in nums:
            return n
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 0.1
                break
        nums.append(n + 10)
        for i in range(len(nums) - 1):
            index = int(abs(nums[i]))
            nums[index] = -nums[index]
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
# 方法一：bit ,因为a^b^b =a
class Solution_bit(object):
    def missingNumber(self, nums):
        x = 0
        for i in range(len(nums)):
            x = x ^ i ^ nums[i]
        i += 1  #记住这里跳出循环时不等于len(nums)
        return x^i  #nums的长度比少一位

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
if __name__ == '__main__':
    n = [0]
    s = Solution_bit()
    print s.missingNumber(n)