# -*- encoding: utf-8 -*-

# 一维
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        f = [0 for i in range(m+1)]
        for i in range(m+1):
            f[i] = 0
        n = len(A)
        for i in range(n):
            for j in range(m, A[i]-1, -1):
                f[j] = max(f[j], f[j - A[i]] + V[i])
        return f[m]

# 二维
def backPackII(self, m, A, V):
    # write your code here
    n = len(A)
    if n <= 0:
        return 0
    f = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(0, m + 1):
            f[i][j] = f[i - 1][j]
            if j >= A[i - 1]:
                f[i][j] = max(f[i][j], f[i - 1][j - A[i - 1]] + V[i - 1])
    return f[n][m]

if __name__ == "__main__":
    s = Solution()
    m = 10
    s1 = [2, 3, 5, 7]
    s2 = [1, 5, 2, 4]

    print s.backPackII(m, s1, s2)