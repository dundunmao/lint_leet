# 1级
# -*- encoding: utf-8 -*-
# 题目：各位相加，sum后再相加，知道剩个位数为止
# 思路：双层循环。或者求9的余数
class Solution(object):
    def _addDigit(self,num):
        result = 0
        for i in range(0,len(str(num))):
            result += num%10
            num = num/10
        return result
    def addDigits(self, num):
        while int(len(str(num)))>1:
            num = self._addDigit(num)
        return num


#另一种方法就是求9的余数,因为 N % 9 = a[0] + a[1] + ..a[n]
def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

if __name__=='__main__':
    # #case1:illegal input
    # n = '123'
    # print add(n)

    #case2:illegal input
    s = Solution()
    n = 38
    print s.addDigits(n)

    # #case3:illegal input
    # n = 1
    # print add(n)