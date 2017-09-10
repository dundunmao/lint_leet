# -*- encoding: utf-8 -*-
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        e = n
        while s + 1 < e:
            mid = s + (e - s) / 2
            x = self.sum_l(mid)
            if x > n:
                e = mid
            elif x < n:
                s = mid
            else:
                return mid
        if self.sum_l(e) <= n:
            return e
        else:
            return s

    def sum_l(self, r):
        res = (1 + r) * r / 2
        return res