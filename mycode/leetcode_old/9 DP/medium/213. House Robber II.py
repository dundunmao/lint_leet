# -*- encoding: utf-8 -*-
# 题目；抢劫房子,list里的数为房子里的钱,连着的房子不能抢,问最多能抢多少钱.这回房子排列是个圈
#

def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0: return 0
    if n < 4: return max(nums)   #只有三家的时候,只能抢一家

    first, second = 0, 0
    for i in nums[:-1]:         #最后一个不算在内
        first, second = second, max(first + i, second)
    result = second

    first, second = 0, 0
    for i in nums[1:]:         #第一个不算在内
        first, second = second, max(first + i, second)
    return max(result, second)   #求两种情况的最大



