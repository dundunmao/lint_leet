# -*- encoding: utf-8 -*-
# 题目：给字母，推数字
# 思路，26**3*m+26**2*k+26**1*j +26**0*i ,注意，幂是**，不是^
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        d['A']=1
        d['B']=2
        d['C']=3
        d['D']=4
        d['E']=5
        d['F']=6
        d['G']=7
        d['H']=8
        d['I']=9
        d['J']=10
        d['K']=11
        d['L']=12
        d['M']=13
        d['N']=14
        d['O']=15
        d['P']=16
        d['Q']=17
        d['R']=18
        d['S']=19
        d['T']=20
        d['U']=21
        d['V']=22
        d['W']=23
        d['X']=24
        d['Y']=25
        d['Z']=26


        num = 0
        le = list(s)
        for i in range(0,len(le)):
            num = num+26**i*d[le[len(le)-1-i]]
        return num

if __name__ == "__main__":

    s = Solution()
    print s.titleToNumber("A")