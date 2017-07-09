# coding:utf-8
# 给一个01矩阵，求不同的岛屿的个数。
#
# 0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 在矩阵：
#
# [
#   [1, 1, 0, 0, 0],
#   [0, 1, 0, 0, 1],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 1]
# ]
# 中有 3 个岛.
from mycode.datastructure.queue import Queue
class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs_fill(grid,i,j)
                    count+=1
        return count
    def bfs_fill(self,grid,x,y):
        grid[x][y] = False
        n = len(grid)
        m = len(grid[0])
        q = Queue()
        id = x*m + y
        q.put(id)
        while q.qsize() != 0:
            id = q.get()
            i = id / m
            j = id % m
            if i > 0 and grid[i-1][j]:
                q.put((i-1)*m+j)
                grid[i-1][j] = False
            if i < n-1 and grid[i+1][j]:
                q.put((i+1)*m+j)
                grid[i+1][j] = False
            if j>0 and grid[i][j-1]:
                q.put(i*m+j-1)
                grid[i][j-1] = False
            if j < m - 1 and grid[i][j+1]:
                q.put(i * m + j+1)
                grid[i][j+1] = False
if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]]

    s = Solution()
    print s.numIslands(grid)
