# coding:utf-8
# 给出两个字符串，找到最长公共子串，并返回其长度。
#
#
#
#  注意事项
#
# 子串的字符应该连续的出现在原字符串中，这与子序列有所不同。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出A=“ABCD”，B=“CBCE”，返回 2
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        ans = 0
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                l = 0
                while i + l < len(A) and j + l < len(B) \
                    and A[i + l] == B[j + l]:
                    l += 1
                if l > ans:
                    ans = l
        return ans