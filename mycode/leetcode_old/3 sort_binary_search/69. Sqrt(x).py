# -*- encoding: utf-8 -*-
# 3级,硬背
# 题目：实现int sqrt(int x)
# 思路：cur = pre/2 + x/(2*pre)
class Solution:
# @param x, an integer
# @return an integer
    def mySqrt(self, x):
        i=1.0
        while(True):
            j=(i+x/i)/2.0
            if(abs(i-j)< 0.000000000005):
                break
            i=j
        return int(j)