# -*- encoding: utf-8 -*-
# 给了一个二位数字，代表一个棋盘地图，1代表岛屿占用的地方，其他地方为海, 1一定会围成一个岛，那么求岛的周长。
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if j == 0 or grid[i][j - 1] == 0: #j=0是其上是空，grid[i][j - 1]是其上是空
                    res += 1
                if i == 0 or grid[i - 1][j] == 0: # 其左是空
                    res += 1
                if j == n - 1 or grid[i][j + 1] == 0: # 其下是空
                    res += 1
                if i == m - 1 or grid[i + 1][j] == 0:  # 其右是空
                    res += 1
        return res

#先遇到1就把4个边都加上，然后check如果什么情况就减掉2个边
class Solution_leet(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += 4
                if i > 0 and grid[i - 1][j] == 1: #如果不把左右边，并且左边是空
                    res -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    res -= 2
        return res

if __name__ == "__main__":
    nums = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    x = Solution()
    print x.islandPerimeter(nums)