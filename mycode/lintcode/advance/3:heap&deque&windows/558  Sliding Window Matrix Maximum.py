class Solution:
    # @param {int[][]} matrix an integer array of n * m matrix
    # @param {int} k an integer
    # @return {int} the maximum number
    def maxSlidingMatrix(self, matrix, k):
        # Write your code here
        m = len(matrix)
        if m == 0 or m < k:
            return 0
        n = len(matrix[0])
        if n == 0 or n < k:
            return 0

        sum = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(m+1):
            sum[i][0] = 0
        for j in range(n+1):
            sum[0][j] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                sum[i][j] = matrix[i - 1][j - 1] +sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

        max_value = float('-inf')
        for i in range(k,m+1):
            for j in range(k,n+1):
                value = sum[i][j] - sum[i - k][j] -sum[i][j - k] + sum[i - k][j - k]
                if value > max_value:
                    max_value = value
        return max_value