# coding:utf-8
#  将两个整数相除，要求不使用乘法、除法和 mod 运算符。
#
# 如果溢出，返回 2147483647 。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给定被除数 = 100 ，除数 = 9，返回 11。
import math
class Solution:
    """
    @param: dividend: the dividend
    @param: divisor: the divisor
    @return: the result
    """

    def divide(self, dividend, divisor):
        # write your code here
        if dividend == 0:
            return 0
        if divisor == 0:
            return None
        if dividend < 0 and divisor < 0:
            flag = 1
        elif dividend < 0 and divisor > 0:
            flag = 0
        elif dividend > 0 and divisor < 0:
            flag = 0
        else:
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        s = 0
        end = dividend
        x, y = self.helper(divisor)
        for i in range(x):
            end = (s + end) // 2
        if y > 0:
            result = end - 1
        else:
            result = end
        if flag:
            return result
        else:
            return -result
    def helper(self, divisor):
        count = math.log(divisor,2)
        if 2**int(count) < divisor:
            return int(count),1
        else:
            return int(count),0

if __name__ == "__main__":
    a = 10
    b = 3

    # [6, 5, 7],
    # [4, 1, 8, 3]
    s = Solution()
    # print s.helper(b)
    print s.divide(a,b)