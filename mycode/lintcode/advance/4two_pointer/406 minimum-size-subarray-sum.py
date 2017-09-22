# -*- encoding: utf-8 -*-
# o(n) two pointer

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if nums == [] or nums is None:
            return 0
        if s == 0:
            return 0
        #           normal case
        le = len(nums)
        i = 0
        sum = 0
        ans = float('inf')
        # 每次j往前走一个，sum把j的值加上，一旦发现sum超了，就不断的让i往前走，边走边查，边吐让出来的数
        for j in range(le):
            sum += nums[j]
            while sum >= s: #一旦发现sum超了
                if j - i + 1 >= 0:
                    ans = min(ans, j - i + 1)
                sum -= nums[i]
                i += 1
        if ans == float('inf'):
            return 0
        else:
            return ans
