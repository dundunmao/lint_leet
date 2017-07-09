# -*- encoding: utf-8 -*-
# 3级
# 题目：Given two binary strings, return their sum (also a binary string). 二进制加法
# 思路：用recursion，讨论三种情况。当最后一位都是0，都是1，一个0一个1。

class Solution:
    #if last digit is both 1,both 0, one 1 one 0
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'