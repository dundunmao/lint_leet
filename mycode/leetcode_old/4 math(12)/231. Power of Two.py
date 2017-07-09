# -*- encoding: utf-8 -*-
# 标签：math，2进制
# 题目；判断给定的int是不是2的幂
# 思路： 16 = b1000, 16 - 1 = b0111, and 16 & 16 - 1 = b1000 & b0111 = 0,
# (&:参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0)

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)