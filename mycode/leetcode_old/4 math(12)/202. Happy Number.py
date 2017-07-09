# -*- encoding: utf-8 -*-
# 题目：digit平方和，直到等于1，就是happy number
# 思路：和258题类似，双层循环，我是单独写了一个函数。最后要限制外层循环的限制。

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i= 0
        while len(str(n))>=1:
            i+=1
            if i>100:
                return False
            if n == 1:
                return True
            n = self.square_sum(n)
        else:
            return False

    def square_sum(self,s):
        sum = 0
        s = list(str(s))
        for i in range(0,len(s)):
            sum +=(int(s[i]))**2
        # print sum
        return sum


if __name__ =="__main__":
    n = 7
    s = Solution()
    print s.isHappy(n)