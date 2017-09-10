# -*- encoding: utf-8 -*-
#这个有用并查集，bfs两种方法。
class union_find:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.root = [0 for i in range(n + 1)]
        self.count = n

    def find(self, x):
        if self.root[x] == 0:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.root[root_a] = root_b
            self.count -= 1

    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self):
        return self.count

    def set_count(self,total):
        self.count = total

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        island = union_find(n*m)

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total += 1
        island.set_count(total)
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i>0 and grid[i-1][j]:
                        island.connect(i * n + j, (i - 1) * n + j)
                    if i < m - 1 and grid[i + 1][j]:
                        island.connect(i * n + j, (i + 1) * n + j)
                    if j > 0 and grid[i][j - 1]:
                        island.connect(i * n + j, i * n + j - 1)
                    if j < n - 1 and grid[i][j + 1]:
                        island.connect(i * n + j, i * n + j + 1)
        return island.query()


# 方法二: BFS
# 从一个点出发，上下左右扩展，能扩展的queue里，每次从queue里拿node进行一次bfs
# 复杂度：每个点只能参与一次bfs，所以是O（n）
from Queue import Queue
class Solution1:
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
# dfs
# 这题用bfs不好,因为如果都是1,每个点都要遍历，递归深度太高，达到了n*m.
# 是一个染色问题,从一个点出发去看在不在一个联通块,在的话,染色(标记).
# 再看下一个点,如果这个点即没染色,又是1,那么从这个点出发,遍历,如果走到已经染过色的,就不走.

class Solution2:
    def __init__(self):
        self.m = 0
        self.n = 0
    def numIslands(self, grid):
        self.m = len(grid)
        if self.m == 0:
            return 0
        self.n = len(grid[0])
        if self.n == 0:
            return 0
        result = 0
        for i in range(self.m):
            for j in range(self.n):
                if not grid[i][j]:   #如果为0(无岛屿)或为false(已经染色)
                    continue
                result+=1           #如果为1, result自加1,
                self.dfs(grid,i,j)  #然后把相邻的1都染色
        return result
    def dfs(self,grid,i,j):         #染色的过程
        if i<0 or i>= self.m or j<0 or j>=self.n:   #如果越界就return
            return
        if grid[i][j]:               #如果为1,
            grid[i][j] = False       #就染色
            self.dfs(grid, i - 1, j) #把他的前后作为为1的也染色
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)


if __name__ == '__main__':
    grid = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
    s = Solution2()
    print s.numIslands(grid)