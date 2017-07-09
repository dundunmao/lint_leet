# -*- encoding: utf-8 -*-
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # edge case
        if len(nums) == 0:
            return 0
        # normal
        hash = {}
        result = 0
        for i in range(len(nums)):
            if k == 0:
                if hash.has_key(nums[i]) and hash[nums[i]] == 1:
                    result += 1
                else:
                    hash[nums[i]] = 1
            else:
                if not hash.has_key(nums[i]):
                    hash[nums[i]] = 1
                    if hash.has_key(nums[i] + k):
                        result += hash[nums[i] + k]
                    elif hash.has_key(nums[i] - k):
                        result += hash[nums[i] - k]
                    if not hash.has_key(nums[i]):
                        hash[nums[i]] = 1
        return result
if __name__ == "__main__":
    a = [3,1,4,1,5]
    k = 2
    x = Solution()
    print x.findPairs(a,k)
