# -*- encoding: utf-8 -*-
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
#
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
#
# Example 1:
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
#
# Example 2:
# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash = {0:-1}
        sum = 0
        maxi = 0
        for i in range(0,len(nums)):
            sum += nums[i]
            if sum == k:
                maxi = i + 1
            elif hash.has_key(sum-k):
                maxi = max(maxi,i-hash[sum-k])
            if not hash.has_key(sum):
                hash[sum] = i
        return maxi
if __name__ == '__main__':
    a = [1,0,-1]
    k = -1
    s = Solution()
    print s.maxSubArrayLen(a,k)