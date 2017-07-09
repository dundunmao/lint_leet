# -*- encoding: utf-8 -*-
# "不同的路径" 的跟进问题：
#
# 现在考虑网格中有障碍物，那样将会有多少条不同的路径？
#
# 网格中的障碍和空位置分别用 1 和 0 来表示。
#
#  注意事项
#
# m 和 n 均不超过100
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 如下所示在3x3的网格中有一个障碍物：
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 一共有2条不同的路径从左上角到右下角。
class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[0 for col in range(n)] for row in range(m)]
        for i in range(0, m):
            if obstacleGrid[i][0] != 1:
                paths[i][0] = 1
            else:
                break

        for j in range(0, n):
            if obstacleGrid[0][j] != 1:
                paths[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
                else:
                    paths[i][j] = 0

        return paths[m - 1][n - 1]

# 自己练习
class Solution4:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code
        # edge case
        if obstacleGrid[0][0] == 1:
            return 0
        # initial
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[None for i in range(n)] for j in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
        if f[0][0] == 0:
            return 0
        else:
            f[0][0] = 1
        for i in range(1,n):
            if f[0][i] != 0:
                f[0][i] = f[0][i-1]
        for j in range(1,m):
            if f[j][0] != 0:
                f[j][0] = f[j-1][0]

        for i in range(1,m):
            for j in range(1,n):
                if f[i][j] != 0:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]
if __name__ == '__main__':
    s = Solution4()
    x = [[0,0],[0,0],[0,0],[1,0],[0,0]]
    print s.uniquePathsWithObstacles(x)