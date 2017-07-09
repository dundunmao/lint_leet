# -*- encoding: utf-8 -*-
#长度*2
class Solution:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums, 0, len(nums)-2), self.helper(nums, 1, len(nums)-1))
    def helper(self, nums, start, end):
        f = [0,0]
        if start == end:
            return nums[end]
        if start + 1 == end:
            return max(nums[start], nums[end])
        f[start%2] = nums[start]
        f[(start+1)%2] = max(nums[start], nums[start+1])
        for i in range(start+2, end+1):
            f[i%2] = max(f[(i-1)%2], f[(i-2)%2]+nums[i])
        return f[end%2]
#切开后考虑头取不取两种情况
class Solution1:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        f = [0 for i in range(n + 1)]
        # 不取第一个
        f[0] = 0
        f[1] = 0
        f[2] = nums[1]
        for i in range(3, n + 1):
            f[i] = max(f[i - 2] + nums[i - 1], f[i - 1])
        result = f[n]
        # print result
        # 取第一个
        f[0] = 0
        f[1] = nums[0]
        for i in range(2, n):
            f[i] = max(f[i - 2] + nums[i - 1], f[i - 1])
        # print f[n-1]
        return max(f[n - 1], result)