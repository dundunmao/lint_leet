# coding:utf-8
# 题目:m*n的方格子,里面有0或者1,0可以走1不可以走,问走到右下角共有多少种走法
# 思路: 把第一行和第一列的0和1反过来.其他格子如果是0,它等于他前面和上面的格子的sum.,如果不是0,就变成0.
# 最后右下角的数就是那个数



class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, n): #第一行每个格子跟前面的数叠加
            if not obstacleGrid[0][i]: #如果这个格子是0
                obstacleGrid[0][i] = obstacleGrid[0][i-1] #则这个格子的值就是本身+前面的格子的值
            else:
                obstacleGrid[0][i] = 0 #如果是1这个数就变为0

        for i in range(1, m):
            if not obstacleGrid[i][0]:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            else:
                obstacleGrid[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]+obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[-1][-1]
