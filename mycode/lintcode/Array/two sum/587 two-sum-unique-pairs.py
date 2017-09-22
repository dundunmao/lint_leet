# -*- encoding: utf-8 -*-
# Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# Given nums = [1,1,2,45,46,46], target = 47
# return 2
#
# 1 + 46 = 47
# 2 + 45 = 47

#
# 边check边加入hash，为了避免pair的重复，下面顺序不能乱
# 1：先check target-nums[i]在不在hash的key里，
#         1.1 如果在，就说明找到了一对，所以res+=1,并且该key标志成True（表明用过了）
#         1.2 同时要看这个nums[i]在不在hash,不在就要往hash里加，但是这时候他的value也是True，因为他也用过了
# 2：else的情况，就是直接往hash里看nums[i]需不需要加进去，加进去是value是False，因为没用过

class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if len(nums) < 2:
            return 0
        hash = {}
        res = 0
        for i in range(len(nums)):
            if target - nums[i] in hash and hash[target - nums[i]] == False:
                res += 1
                hash[target - nums[i]] = True
                if nums[i] not in hash:
                    hash[nums[i]] = True
            elif nums[i] not in hash:
                hash[nums[i]] = False
        return res

# 比上面在简化一点，每次check发现找到 （target-nums[i]）在hash里时，这个nums[i]都不用加进hash
class Solution1:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if len(nums) < 2:
            return 0
        hash = {}
        res = 0
        for i in range(len(nums)):
            if target - nums[i] in hash:
                if hash[target - nums[i]] == False:
                    res += 1
                    hash[target - nums[i]] = True
            elif nums[i] not in hash:
                hash[nums[i]] = False
        return res