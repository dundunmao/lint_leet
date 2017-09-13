# -*- encoding: utf-8 -*-
# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.匹配任意字符
# '*' Matches zero or more of the preceding element.代表*前面这个char可以不出现或出现n次
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true  .代表任意字符，*代表任意字符出现了n次
# isMatch("ab", ".*") → true  .代表任意字符，*代表任意字符出现了n次 所以 ".*" 代表任意string
# isMatch("aab", "c*a*b") → true  "c*"可以表示c出现0次，"a*"可以表示a出现2次
#
#方法一：DP
# 从后往前
# 1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
# 2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
# 3, If p.charAt(j) == '*':
#    here are two sub conditions:
#                1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
#                2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
#                               dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a
#                            or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
#                            or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None or p is None:
            return False
        l_s = len(s)
        l_p = len(p)
        f = [[ None for j in range(l_p+1)]for i in range(l_s+1)]
        f[0][0] = True
        for i in range(0, l_p):
            if p[i] == '*' and f[0][i - 1]:
                f[0][i + 1] = True
        for i in range(0, l_s):
            for j in range(0, l_p):
                if p[j] == '.':
                    f[i + 1][j + 1] = f[i][j]
                if p[j] == s[i]:
                    f[i + 1][j + 1] = f[i][j]
                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        f[i + 1][j + 1] = f[i + 1][j - 1]
                    else:
                        f[i + 1][j + 1] = f[i + 1][j] or f[i][j + 1] or f[i + 1][j - 1]
        return f[l_s][l_p]
# 方法2：
class Solution1(object):
    def isMatch(self, s, p):
        if s == '':
            return p == ''
        l_s = len(s)
        l_p = len(p)
        if '*' == p[1]:
            # x* matches empty string or at least one character: x* -> xx*
            # *s is to ensure s is non-empty
            return self.isMatch(s,p[2:]) or s != '' and (s[0] == p[0] or '.' == p[0]) and self.isMatch(s[1:], p)
        else:
            return s != '' and (s[0] == p[0] or '.' == p[0]) and self.isMatch(s[1:], p[1:])
if __name__ == "__main__":
    s = "aa"
    p = "a"
    x = Solution()
    print x.isMatch(s,p)
