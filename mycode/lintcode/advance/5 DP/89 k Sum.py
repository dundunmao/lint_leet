
class Solution1:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        n = len(A)
        # f = [[[None for i in range(target + 1)] for j in range(k + 1)] for k in range(n + 1)]
        f = [[[0 for _ in range(target+1)] for _ in range(k+1)] for _ in range(n+1)]
        f[0][0][0] = 1
        for i in range(1, n + 1):
            for j in range(0, k + 1):
                for t in range(0, target + 1):
                    f[i][j][t] = f[i - 1][j][t]
                    if t >= A[i - 1] and j >= 1:
                        f[i][j][t] = f[i][j][t] + f[i - 1][j - 1][t - A[i - 1]]
        return f[n][k][target]
if __name__ == "__main__":
    s = Solution1()
    A = [1,2,3,4]
    k = 2
    m = 5
    print s.kSum(A,k,m)