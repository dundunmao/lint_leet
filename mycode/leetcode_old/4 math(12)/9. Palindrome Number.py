# -*- encoding: utf-8 -*-
# 标签：math
# 题目；给定的int是不是回文 用[::-1]就是讲列表反过来的意思。另一种方法，一边除10一边乘10
# 思路：
class Solution(object):
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]
 # 或者：
class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            t = -x
        else:
            t = x
        y = 0
        while t != 0:   #这一段是reverse
            y = y*10 + (t % 10) #把原数的除以10的余数（找个位数的意思）填到新的数里面再乘以10
            t //= 10
        return x == y