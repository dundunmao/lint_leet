# -*- encoding: utf-8 -*-
# 设计一个算法，找出只含素因子2，3，5 的第 n 大的数。
#
# 符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
#
#  注意事项
#
# 我们可以认为1也是一个丑数
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 如果n = 9， 返回 10
#O(nlogn) HashMap + Heap
from heapq import *
class Solution:
    """
    @param {int} n an integer.
    @return {int} the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if n <= 1:
            return n
        Q = [1]
        hash = {1:True}
        primes = [2,3,5]
        # for i in range(3):
        #     heappush(Q, primes[i])
        #     hash[primes[i]] = True
        for j in range(n):
            number = heappop(Q)
            for k in range(3):
                if not hash.has_key(primes[k]*number):
                    heappush(Q, primes[k]*number)
                    hash[primes[k]*number] = True
        return number


# because every number can only be divided by 2, 3, 5, one way to look at the sequence is to split the sequence to three groups as below:
# The ugly-number sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15
# (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
# (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
# (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
# 我们就从这里每次都找最小的
# every step，we choose the smallest one, and move one step after,including nums with same value.
class Solution_leet(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [1]
        index2 = index3 = index5 = 1
        factor2 = 2
        factor3 = 3
        factor5 = 5
        for i in range(1,n):
            mini = min(factor2,factor3,factor5)
            q.append(mini)
            if factor2 == mini:
                factor2 = 2*q[index2]
                index2 += 1
            elif factor3 == mini:
                factor3 = 3*q[index3]
                index3 += 1
            elif factor5 == mini:
                factor5 = 5*q[index5]
                index5 += 1
        print q
        return q[-1]

if __name__ == '__main__':
    n = 10
    s = Solution_leet()
    print s.nthUglyNumber(n)