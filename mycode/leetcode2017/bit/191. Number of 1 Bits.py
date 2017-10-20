# -*- encoding: utf-8 -*-
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
# 把十进制用二进制表示，然后return里面有几个1

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n!=0:
            if (n & 1) == 1:
                count += 1 #检查最后一位是不是1，如果是这里count就+1
            n = n>>1   #右移一位，检查下一位
        return count
if __name__ == '__main__':
    a = 3
    s = Solution()
    s.hammingWeight(a)