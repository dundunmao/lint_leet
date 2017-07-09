# coding:utf-8
# 有一个机器人的位于一个 m × n 个网格左上角。
#
# 机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。
#
# 问有多少条不同的路径？
#
#  注意事项
#
# n和m均不超过100
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 m = 3 和 n = 3, 返回 6.
# 给出 m = 4 和 n = 5, 返回 35.
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 

    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        sum = [[0 for col in range(n)] for row in range(m)]
        for i in range(0,m):
            sum[i][0] = 1
        for j in range(0,n):
            sum[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                sum[i][j] = sum[i-1][j]+ sum[i][j-1]
        return sum[m-1][n-1]