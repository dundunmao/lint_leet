# -*- encoding: utf-8 -*-
class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        result = [[None for i in range(2)] for _ in range(2)]
        m = len(matrix)
        n = len(matrix[0])
        if m == 0:
            return result
        if n == 0:
            return result
        # 预处理
        sum = [[None for i in range(n+1)] for _ in range(m+1)]
        for j in range(0,n+1):
            sum[0][j] = 0
        for i in range(1,m+1):
            sum[i][0] = 0
        for i in range(0,m):
            for j in range(0,n):
                sum[i+1][j+1] = matrix[i][j] + sum[i+1][j]+sum[i][j+1]-sum[i][j]
        for l in range(0,m):
            for h in range(l+1,m+1):
                map = {}
                for j in range(0,n+1):
                    diff = sum[h][j]-sum[l][j]
                    if map.has_key(diff):
                        k = map[diff]
                        result[0][0] = l
                        result[0][1] = k
                        result[1][0] = h-1
                        result[1][1] = j-1
                        return result
                    else:
                        map[diff] = j
        return result

