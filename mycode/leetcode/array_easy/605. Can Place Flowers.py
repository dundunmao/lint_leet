# -*- encoding: utf-8 -*-
# 给一个数组[1,0,0,0,1]和一个数n，把里面的0改为1，不能让1连着，问能不能改出n个1来
# 解题：每次找一段连续的0，里面能改的1为其长度的一半
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 1
        result = 0
        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 0:
                count+=1
            else:
                result += (count-1)/2
                count = 0
        if count != 0:
            result += count/2 #把最后一段的0的结果加上
        return result>=n