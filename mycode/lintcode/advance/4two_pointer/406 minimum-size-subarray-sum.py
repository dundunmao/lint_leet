# -*- encoding: utf-8 -*-
# o(n)
class Solution:
    # @param nums: a list of integers
    # @param s: an integer
    # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        i, j = 0, 0
        sum = 0
        ans = float('inf')
        # i,j都从0开始,i固定,j往后走
        for i in range(0, len(nums)):
            while j < len(nums) and sum < s: #j往后走,走到的大于S了,停下
                sum += nums[j]
                j += 1
            if sum >= s:    #记录这个值
                ans = min(ans, j-i)
            sum -= nums[i]  #下一轮i要往后走一步,所以要减掉i上的值
        if ans == float('inf'):
            ans = -1
        return ans

class Solution_leet(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if sum(nums) < s:
            return 0
        l, r, sub_sum = 0, 0, 0
        ans = len(nums) + 1
        size = len(nums)
        while l < size and r <= size: #左右指针都不超届
            if sub_sum >= s:   #如果sub_sum比s大，就更新ans，并且l往后走
                ans = min(ans, r - l) #更新ans
                if 1 == ans:       #但如果ans为1，就是只包括一个数，那就得到最最小的了，直接break得答案
                    return 1
                sub_sum -= nums[l]
                l += 1
            else:          #如果sub_sum比s小：l不动，r继续往后走
                if r < size:
                    sub_sum += nums[r]
                r += 1

        return ans