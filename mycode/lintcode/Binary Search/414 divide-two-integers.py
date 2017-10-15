# coding:utf-8
#  将两个整数相除，要求不使用乘法、除法和 mod 运算符。
#
# 如果溢出，返回 2147483647 。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给定被除数 = 100 ，除数 = 9，返回 11。
# 第一次减9，第二次减9+9=18，第三次减18+18 = 36，第四次减36+36=72，第五次减72+72=144>100了，所以从100-72=28重新减9


class Solution(object):
    def divide1(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if divisor == 0:
            return float('inf')
        flag = True
        if dividend < 0 and divisor > 0:
            flag = False
        if dividend > 0 and divisor < 0:
            flag = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            count, left = self.count(dividend, divisor)
            # print count, left
            res += count
            dividend = left
        # print res
        if flag == False:
            return -res
        else:
            return res

    def count(self, dividend, divisor):
        count = 1
        count_left = 1
        dividend_left = 0
        while dividend - divisor > 0:
            count_left = count
            dividend_left = dividend - divisor
            divisor = divisor + divisor
            count = count * 2

        return count_left, dividend_left
    # 答案
    def divide(self, dividend, divisor):
        # write your code here
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            neg = True
        else:
            neg = False
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        shift = 31
        while shift >= 0:
            if a >= (b << shift):  # 9<<3（左移3位）相当于9 * 2^3=9*8=72
                a -= (b << shift)
                ans += (1 << shift)  #1<<1（左移1位）相当于1 * 2^1=2
            shift -= 1
        if neg:
            ans = - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans

if __name__ == "__main__":
    a = 100
    b = 9
    s = Solution()
    # print s.helper(b)
    print s.divide(a,b)