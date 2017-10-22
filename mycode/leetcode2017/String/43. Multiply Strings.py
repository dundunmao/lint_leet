# -*- encoding: utf-8 -*-
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
# 两个数相乘的结果

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        len3 = len1 + len2

        num3 = [0 for _ in xrange(len3)]
        for i in xrange(len1 - 1, -1, -1):
            carry = 0
            for j in xrange(len2 - 1, -1, -1):
                product = carry + num3[i + j + 1] + int(num1[i]) * int(num2[j])  #把这位该加的都加起来，然后下面在分配
                num3[i + j + 1] = product % 10  # 本位的个位数
                carry = product / 10            # 本位的十位数，留着下一次加进去

            num3[i] = carry

        result = ""
        i = 0
        while i < len3 - 1 and num3[i] == 0:
            i += 1

        while i < len3:
            result += str(num3[i])
            i += 1

        return result

if __name__ == "__main__":
    a = '123'
    b = '456'
    s = Solution()
    print s.multiply(a, b)