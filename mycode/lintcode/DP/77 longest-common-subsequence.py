# coding:utf-8
# 给出两个字符串，找到最长公共子序列(LCS)，返回LCS的长度。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# 最长公共子序列的定义：
#
# 最长公共子序列问题是在一组序列（通常2个）中找到最长公共子序列（注意：不同于子串，LCS不需要是连续的子串）。该问题是典型的计算机科学问题，是文件差异比较程序的基础，在生物信息学中也有所应用。
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# 样例
# 给出"ABCD" 和 "EDCA"，这个LCS是 "A" (或 D或C)，返回1
#
# 给出 "ABCD" 和 "EACB"，这个LCS是"AC"返回 2
class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        n, m = len(A), len(B)
        f = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if A[i-1] == B[j-1]:
                    f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1], f[i-1][j-1]+1)
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1])
        return f[n][m]