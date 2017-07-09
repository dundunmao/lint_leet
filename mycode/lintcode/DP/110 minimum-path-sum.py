# -*- encoding: utf-8 -*-
# 给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。
#
#
#
#  注意事项
#
# 你在同一时间只能向下或者向右移动一步
class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        sum = [ [float('inf') for col in range(n)] for row in range(m)]  #这个地方mn顺序要注意
        sum[0][0] = grid[0][0]
        for i in range(1,m):
            sum[i][0] = sum[i-1][0]+grid[i][0]
        for j in range(1,n):
            sum[0][j] = sum[0][j-1]+grid[0][j]
        i,j = 0,0
        for i in range(1, m):
            for j in range(1,n):
                sum[i][j] = min(sum[i-1][j],sum[i][j-1]) + grid[i][j]
        return sum[m-1][n-1]