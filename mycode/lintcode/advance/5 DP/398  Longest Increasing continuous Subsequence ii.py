# -*- encoding: utf-8 -*-
class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def __init__(self):
        self.m = 0
        self.n = 0
        self.f = []
        self.flag = []
    def longestIncreasingContinuousSubsequenceII(self, A):
        # Write your code here
        if len(A) == 0:
            return 0
        result = 0
        self.m = len(A)
        self.n = len(A[0])
        self.f = [[0 for i in range(self.n)] for j in range(self.m)]
        self.flag = [[0 for i in range(self.n)] for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.f[i][j] = self.search(i,j,A)
                result = max(result, self.f[i][j])
        return result
    def search(self, x, y, A):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        if self.flag[x][y] != 0:
            return self.f[x][y]
        ans = 1
        nx = 0
        ny = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>= 0 and nx<self.m and ny>=0 and ny<self.n:
                if A[x][y] > A[nx][ny]:
                    ans = max(ans, self.search(nx,ny,A)+1)
        self.flag[x][y] = 1
        self.f[x][y] = ans
        return ans


