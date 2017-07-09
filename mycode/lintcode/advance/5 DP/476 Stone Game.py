# -*- encoding: utf-8 -*-
# linz方法
class Solution1:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        if A is None or len(A) == 0:
            return 0
        n = len(A)
         # initialize
        f = [[None for i in range(n)] for j in range(n)]
        for i in range(n):
            f[i][i] = 0
        # preparation
        sum = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            sum[i][i] = A[i]
            for j in range(i+1, n):
                sum[i][j] = sum[i][j-1] + A[j]
        for length in range(2,n+1): #枚举长度
            if n<=n-length+1:
                start = n
            else:
                start = n-length+1
            for i in range(0,start):  #枚举起点
                j = i + length - 1  # 尾点
                f[i][j] = float('inf')
                for k in range(i,j):
                    f[i][j] = min(f[i][j],
                                  f[i][k]+f[k+1][j]+sum[i][j])
        return f[0][n-1]
#我的错误的枚举i,j,k的方法
class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        if A is None or len(A) == 0:
            return 0
        n = len(A)
         # initialize
        f = [[None for i in range(n)] for j in range(n)]
        visit = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            f[i][i] = 0
        # preparation
        sum = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            sum[i][i] = A[i]
            for j in range(i+1, n):
                sum[i][j] = sum[i][j-1] + A[j]
        for i in range(0,n-1):
            for j in range(i+1,n):
                f[i][j] = float('inf')
                for k in range(i,j):
                    f[i][j] = min(f[i][j],
                                  f[i][k]+f[k+1][j]+sum[i][j])



# 方法一:记忆化
class Solution2:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        if A is None or len(A) == 0:
            return 0
        n = len(A)
         # initialize
        f = [[0 for i in range(n)] for j in range(n)]
        visit = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            f[i][i] = 0
        # preparation
        sum = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            sum[i][i] = A[i]
            for j in range(i+1, n):
                sum[i][j] = sum[i][j-1] + A[j]
        return self.search(0, n-1, f, visit, sum)

    def search(self, l, r, f, visit, sum):
        if visit[l][r] == 1:
            return f[l][r]
        if l == r:
            visit[l][r] = 1
            return f[l][r]
        f[l][r] = float('inf')
        for k in range(l,r):
            f[l][r] = min(f[l][r],
                          self.search(l,k,f,visit,sum)+self.search(k+1,r,f,visit,sum)+sum[l][r])
        visit[l][r] = 1
        return f[l][r]
# 方法二: for 循环
class Solution3:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        n = len(A)
        if n == 0:
            return 0
        f = [[0 for i in range(n)] for j in range(n)]
        sums = [0 for i in range(n + 1)]
        sums[0] = 0
        for i in range(0,n):
            for j in range(i,n):
                f[i][j] = float('inf')
        for i in range(0, n):
            f[i][i] = 0
            sums[i+1] = sums[i] + A[i]
        return self.search(0,n-1,f,sums)
    def search(self, start, end, f, sums):
        if f[start][end] != float('inf'):
            return f[start][end]
        mini = float('inf')
        for k in range(start,end):
            left = self.search(start,k,f,sums)
            right = self.search(k+1,end,f,sums)
            now = sums[end+1]-sums[start]
            mini = min(mini,left+right+now)
        f[start][end] = mini
        return mini

if __name__ == "__main__":
    s = Solution1()
    A = [3,4,3]
    print s.stoneGame(A)