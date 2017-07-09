# -*- encoding: utf-8 -*-
class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame2(self, A):
        # Write your code here
        n = len(A)
        if n <= 1:
            return 0
        f = [[0 for i in range(n*2)] for j in range(n*2)]
        sums = [0 for i in range(n*2 + 1)]
        for i in range(1,n*2+1):
            sums[i] = sums[i-1]+A[(i-1)%n]
        for i in range(0,n*2):
            f[i][i] = 0
        for length in range(2,n*2+1):
            if n * 2 <= n * 2 - length + 1:
                start = n*2
            else:
                start = n * 2 - length + 1
            for i in range(0,start):
                j = i+length-1
                f[i][j] = float('inf')
                for k in range(i,j):
                    f[i][j] = min(f[i][j],f[i][k]+f[k+1][j]+sums[j+1]-sums[i])
        ans = float('inf')
        for i in range(0,n):
            ans=min(ans,f[i][i+n-1])
        return ans

if __name__ == "__main__":
    s = Solution()
    A = [1,1,4,4]
    print s.stoneGame2(A)