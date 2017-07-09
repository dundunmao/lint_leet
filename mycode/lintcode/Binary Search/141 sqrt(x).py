# coding:utf-8

# 实现 int sqrt(int x) 函数，计算并返回 x 的平方根。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# sqrt(3) = 1
#
# sqrt(4) = 2
#
# sqrt(5) = 2
#
# sqrt(10) = 3

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        start = 1
        end = x
        while start+1 < end:
            mid = start+(end-start)/2
            if mid*mid <= x:
                start = mid
            else:
                end = mid
        if end*end <=x:
            return end
        return start

    def mySqrt_leet(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0
        if x == 1:
            return 1
        start = 1
        end = x
        while start + 1 < end:
            mid = (start+end)/2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                start = mid
            else:
                end = mid
        return start
if __name__ == "__main__":
    x = 10
    s = Solution()
    print s.sqrt(x)
