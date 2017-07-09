# -*- encoding: utf-8 -*-
# 题目：给数字，推字母
# 思路：两层循环，求余数求整除数。

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d={}
        d[0]='Z'
        d[1]='A'
        d[2]='B'
        d[3]='C'
        d[4]='D'
        d[5]='E'
        d[6]='F'
        d[7]='G'
        d[8]='H'
        d[9]='I'
        d[10]='J'
        d[11]='K'
        d[12]='L'
        d[13]='M'
        d[14]='N'
        d[15]='O'
        d[16]='P'
        d[17]='Q'
        d[18]='R'
        d[19]='S'
        d[20]='T'
        d[21]='U'
        d[22]='V'
        d[23]='W'
        d[24]='X'
        d[25]='Y'
        d[26]='Z'
        temp = n
        digit = []
        result = []
        while temp >= 1:
            a = temp % 26
            digit.append (a)
            temp /= 26
            if a == 0:
                temp -= 1
        for i in range(len(digit)-1,-1,-1):
            result.append(d[digit[i]])
        return ''.join(result)