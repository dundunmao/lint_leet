class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):
        # Write your code here
        n = len(A)
        f = [0 for i in range(m + 1)]
        for i in range(n):
            for j in range(A[i],m+1):
                f[j] = max(f[j], f[j - A[i]]+V[i])
        return f[m]
#     2d version
class Solution1:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):
        # Write your code here
        n = len(A)
        f = [[0 for i in range(m + 1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(m+1):
                if j >= A[i-1]:
                    f[i][j] = max(f[i][j-A[i-1]]+V[i-1], f[i][j])
        return f[n][m]