# -*- encoding: utf-8 -*-
# happy number 如例子：
# 19 is a happy number
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 把数字如下处理，最后或者是happy的或者会是个cycle。所以这道题不会无限下去，如果不happy会有环，
# 有环的问题可以想到用two pointer的slow fast追击
# 或者用hash看有没有重复出现的东西
# 方法一： 追击
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.digit_ss(n)
        fast = self.digit_ss(slow)
        while slow != fast:
            slow = self.digit_ss(slow)
            fast = self.digit_ss(fast)
            fast = self.digit_ss(fast)
        if slow == 1:
            return True
        else:
            return False
    def digit_ss(self,n):
        sum = 0
        while n != 0:
            tmp = n % 10
            sum += tmp**2
            n = n / 10
        return sum
# 方法二：hash
class Solution_hash(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hash = {}
        while n != 1:
            if hash.has_key(n):
                return False
            else:
                hash[n] = 1
                n = self.digit_ss(n)
        return True
    def digit_ss(self,n):
        sum = 0
        while n != 0:
            tmp = n % 10
            sum += tmp**2
            n = n / 10
        return sum


if __name__ == '__main__':
    n= 19
    s = Solution_hash()
    print s.isHappy(n)