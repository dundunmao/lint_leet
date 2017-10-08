# -*- encoding: utf-8 -*-
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

# # 解：各字母代表的数字是 dict = {'I':1,    'V':5,  'X':10, 'L':50, 'C':100,'D':500,'M':1000}
# 方法是如果大的在小的前面，就是加，反过来就是减。记得最后一位不能比，要单独加进去
# 给个排行如下：hash  = {'I':1,  'V':2,  'X':3,  'L':4,  'C':5,  'D':6,  'M':7}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        hash = {'I': 1, 'V': 2, 'X': 3, 'L': 4, 'C': 5, 'D': 6, 'M': 7}
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s) - 1):
            if hash[s[i]] < hash[s[i + 1]]:
                sum -= dict[s[i]]
            else:
                sum += dict[s[i]]
        sum += dict[s[len(s) - 1]]
        return sum
