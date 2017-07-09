# -*- encoding: utf-8 -*-
import collections
class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        m = len(grid)
        n = len(grid[0])
        dist = [[float('inf') for i in range(n)] for j in range(m)]
        count = [[ 0 for i in range(n)] for j in range(m)]
        result = float('inf')
        building = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  #遇到一房子
                    self.bfs(grid, i, j, dist, m, n, count)  #就计算它到每一个0的距离,更新在dist的矩阵里
                    building += 1     #房子个数统计
        for i in range(m):
            for j in range(n):
                if count[i][j] == building and dist[i][j] < result: #所以房子都能到达这,总距离小于result
                    result = dist[i][j]                             # result就更新
        if result != float('inf'):
            return result
        else:
            return -1
        #对于grid里的(i，j)这个房子,算出它到每一个'0'的距离,更新在dist里,
        # 同时记录在reachable_count+=1,这个矩阵是更新每个'0',有几个房子到达过这
    def bfs(self, grid, i, j, dist, m, n, count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = collections.deque([(i, j, 0)]) #从(i,j)这个房子出发,到此点的距离是0

        while q:
            i, j, l = q.popleft()
            if dist[i][j] == float('inf'):#说明没有房子来访问过,从0开始计数.
                dist[i][j] = 0
            dist[i][j] += l  # 在dist的这个位置加上此点到(i,j)这个房子的距离

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i + x, j + y

                if nx > -1 and nx < m and ny > -1 and ny < n and not visited[nx][ny]:#没越界也没visit过
                    visited[nx][ny] = True  #记录为visit
                    if grid[nx][ny] == 0:  #如果这里可以建邮局
                        q.append((nx, ny, l + 1))  #把这个'0'的坐标和房子到这个'0'的距离放q里.(注意这个距离现在是放在q里,还没更新在dist里)
                        count[nx][ny] += 1  #距离的计数
