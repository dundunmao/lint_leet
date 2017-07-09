# -*- encoding: utf-8 -*-
# 题目:给一个array和一个数k，在array里找对子，使得其diff=k，问有几对,注意array值可以是负的。
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# 解题：把数组放hash里，value=1，遇到重复的，value+=1
#      如果k=1就看有多少value >1的
#      如果k不为1，每traverse一个key,就找hash里有没有key+k这个key。不管正负，
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # edge case
        if len(nums) == 0 or k < 0:
            return 0
        # normal
        hash = {}
        result = 0
        for num in nums:
            if hash.has_key(num):
                hash[num] += 1
            else:
                hash[num] = 1
        for key,value in hash.items():
            if k == 0:
                if value > 1:
                    result += 1
            else:
                if hash.has_key(key+k):
                    result += 1
        # for i in range(len(nums)):
        #     if hash.has_key(nums[i] - k):
        #         result += hash[nums[i] - k]
        #         hash[nums[i]] = 1
        #     elif hash.has_key(k - nums[i]):
        #         result += hash[k - nums[i]]
        #     if hash.has_key(nums[i]):
        #         hash[nums[i]] += 1
        #     else:
        #         hash[nums[i]] = 1
        return result
if __name__ == "__main__":
    a = [-3, -1, 4, 1, 5]
    k = 2
    x = Solution()
    print x.findPairs(a,k)