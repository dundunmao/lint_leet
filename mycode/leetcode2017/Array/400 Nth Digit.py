# coding: utf-8
# 1-9 9个
# 10-99 90个
# 100-999 900个
# 9 * 10 ** i * (i + 1)确定是在哪个范围内
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        i = 0
        while n > 0:
            rest = n
            n -= 9 * 10 ** i * (i + 1)
            i += 1
        digit = i
        x = rest / digit  #第几个数
        y = rest % digit  #那个数的第几位
        if y == 0:
            result = 10 ** (digit - 1) + x - 1
        else:
            # result = str(x + 1)[rest - 1]
            result = 10**(digit-1)+x
        result = str(result)[y-1]

        return int(result)
if __name__ == "__main__":
    s = Solution()
    n = 28
    print s.findNthDigit(n)