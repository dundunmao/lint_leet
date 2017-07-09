class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
        n = len(A)
        f = [[float('inf') for i in range(101)] for j in range(n+1)]
        # for i in range(n+1):
        #     for j in range(101):
        #         f[i][j] = float('inf')
        for i in range(101):
            f[0][i] = 0
        for i in range(n+1):
            for j in range(101):
                if f[i-1][j] != float('inf'):
                    for k in range(max(0,j-target),min(100,j+target)+1):
                        if abs(j-k) <= target:
                            f[i][k] = min(f[i][k], f[i-1][j]+abs(A[i-1]-k))
        ans = float('inf')
        for i in range(101):
            if f[n][i] < ans:
                ans = f[n][i]
        return ans        