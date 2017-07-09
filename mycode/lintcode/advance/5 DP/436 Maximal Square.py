# -*- encoding: utf-8 -*-
class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        if m > 0:
            n = len(matrix[0])
        else:
            return result
        f = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            f[i][0] = matrix[i][0]
            result = max(f[i][0], result)
            for j in range(1,n):
                if i>0:
                    if matrix[i][j]>0:
                        f[i][j] = min(f[i-1][j], min(f[i][j-1], f[i-1][j-1]))+1
                    else:
                        f[i][j] = 0
                else:
                    f[i][j] = matrix[i][j]
                result = max(f[i][j], result)
        return result*result

    def maxSquare1(self, matrix):
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        if m > 0:
            n = len(matrix[0])
        else:
            return result
        f = [[0 for i in range(n)] for j in range(2)]
        for i in range(m):
            f[i%2][0] = matrix[i][0]
            result = max(f[i%2][0], result)
            for j in range(1, n):
                if i > 0:
                    if matrix[i][j] > 0:
                        f[i%2][j] = min(f[(i - 1)%2][j], min(f[i%2][j - 1], f[(i-1)%2][j - 1])) + 1
                    else:
                        f[i%2][j] = 0
                else:
                    f[i%2][j] = matrix[i%2][j]
                result = max(f[i%2][j], result)
        return result * result