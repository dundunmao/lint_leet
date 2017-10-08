# -*- encoding: utf-8 -*-
# •	Map store previous values ( O(N) )
# •	把第一题extend到2D。给一个matrix, all elements are positive，问有没有个sub rectangle加起来和等于target。return true/false。
# •	Lz听到题目有点懵，认真调整心态，解决之。先写了个cumulative sum。把所有从0,0 到i,j的和算在新的matrix的i,j上。方便之后算head到tail的sub rectangle的和。这一步O(n^2)
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
