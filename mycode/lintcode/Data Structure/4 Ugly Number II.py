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



if __name__ == '__main__':
    n = 9
    s = Solution()
    print s.nthUglyNumber(n)