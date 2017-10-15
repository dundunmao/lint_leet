# -*- encoding: utf-8 -*-
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'

class Solution1(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        sb = []
        while i >= 0 or j >= 0:
            sum = carry
            if j >= 0:
                sum += b[j] - '0'
                j -= 1
            if i >= 0:
                sum += a[i] - '0'
                i -= 1
            sb.append(sum % 2)
            carry = sum / 2
        if carry != 0:
            sb.append(carry)
        sb.reverse()
        return ''.join(sb)


if __name__ == '__main__':
    s = Solution1()
    a = '11'
    b = '1'
    print s.addBinary(a,b)