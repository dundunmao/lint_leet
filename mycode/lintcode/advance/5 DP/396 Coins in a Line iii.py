# -*- encoding: utf-8 -*-
#方法一从先手角度出发
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        n = len(values)
        if n < 3:
            return True
        sum = 0
        for i in range(n):
            sum += values[i]
        f = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            f[i][i] = values[i - 1]
        for i in range(1, n):
            f[i][i + 1] = max(values[i - 1], values[i])
        for i in range(n,0,-1):
            for j in range(i + 2, n + 1):
                left = min(f[i + 2][j], f[i + 1][j - 1]) + values[i - 1]
                right = min(f[i][j - 2], f[i + 1][j - 1]) + values[j - 1]
                f[i][j] = max(left, right)
        return f[1][n] > sum / 2

#方法二:从当前人角度出发
class Solution3:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        n = len(values)
        sum = [0 for i in range(n + 1)]
        sum[0] = 0
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + values[i - 1]
        f = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(1,n+1):
            f[i][i] = values[i-1]
        for i in range(n, 0, -1):
            for j in range(i + 1, n + 1):
                s = sum[j] - sum[i - 1]
                f[i][j] = max(s - f[i + 1][j],
                              s - f[i][j - 1])
        return f[1][n] > sum[n] / 2
#九章法
class Solution1:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        n = len(values)
        sum = [0 for i in range(n + 1)]
        sum[0] = 0
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + values[i - 1]
        f = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            f[i][i] = values[i]
        for length in range(2, n + 1):
            for i in range(n):
                j = i + length - 1
                if j >= n:
                    continue
                s = sum[j + 1] - sum[i]
                f[i][j] = max(s - f[i + 1][j],
                              s - f[i][j - 1])
        return f[0][n - 1] > sum[n] / 2
if __name__ == "__main__":
    s = Solution3()
    A = [1,2,3,4]  #T
    # A = [1, 2, 3, 4, 5, 3, 1] #T
    A = [1492,83,760,915,622,183]
    # A = [760,915,622,183]
    print s.firstWillWin(A)