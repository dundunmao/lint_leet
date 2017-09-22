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
# 从后往前如果两个是一样的都是字母，都是'.'。或都是'*'，就是第一种情况。可以同时往前看一位
#
# 1, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1]; 第二种情况是对照组是'.' 也可以同时往前看一位。 eg：("……a","…….")
# 2, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];  eg：("……a","……a")
# 3, If p.charAt(j) == '*': 第二种情况是对照组是'*'，要分两种情况讨论
#      1 if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //如果对照组的*前面的cha跟原组不一样，'char*'被当做empty看待，eg：("……a","……b*")
#      2 if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.': //如果对照组的*前面的cha跟原组一样或是'.'：取下面三种情况的或
#                               dp[i][j] = dp[i-1][j]    //a* 代表多个a 所以是原组往前挪一位,一直可以挪到下面的情况 eg:("……aaa","……a*")
#                            or dp[i][j] = dp[i][j-1]   // a* 代表一个a 所以是对照组往前挪一位 eg:（"……a","……a*"）
#                            or dp[i][j] = dp[i][j-2]   // a* 代表empty 所以是对照著往前挪两位eg:（"……a","…… 。*")
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

if __name__ == "__main__":
    s = "aa"
    p = "a"
    x = Solution()
    print x.isMatch(s,p)
