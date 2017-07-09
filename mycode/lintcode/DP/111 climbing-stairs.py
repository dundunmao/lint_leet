# coding:utf-8
# 假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如n=3，1+1+1=1+2=2+1=3，共有3中不同的方法
#
# 返回 3
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n==0:
            return 1
        if n <= 2:
            return n
        result = [0 for i in range(n)]
        result[0] = 1
        result[1] = 2
        for i in range(2, n):
            result[i] = result[i-1]+result[i-2]
        return result[n-1]