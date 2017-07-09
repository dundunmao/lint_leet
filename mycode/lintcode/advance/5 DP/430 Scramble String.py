# -*- encoding: utf-8 -*-
# 记忆化搜索
class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        hash = {}
        if len(s1) != len(s2):
            return False
        if hash.has_key(s1+"#"+s2):
            return hash[s1+"#"+s2]
        n = len(s1)
        if n == 1:
            return s1[0] == s2[0]
        for k in range(1,n):
            if self.isScramble(s1[0:k],s2[0:k]) and self.isScramble(s1[k:n],s2[k:n])or self.isScramble(s1[0:k],s2[n-k:n]) and self.isScramble(s1[k:n],s2[0:n-k]):
                hash[s1+"#"+s2] = True
                return True
        hash[s1+"#"+s2] = False
        return False
#递推
class Solution1:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        n = len(s1)
        dp = [[[None for i in range(n+1)] for j in range(n)] for k in range(n)]
        for i in range(0,n):
            for j in range(0,n):
                dp[i][j][1] = s1[i] == s2[j]
        for length in range(2,n+1):
            if n < n-length:
                flag1 = n-1
            else:
                flag1 = n-length+1
            for x in range(0, flag1):
                if n<n-length:
                    flag2 = n-1
                else:
                    flag2 = n-length+1
                for y in range(0,flag2):
                    for k in range(1,length):
                        dp[x][y][length] = (dp[x][y][k] and dp[x+k][y+k][length-k]) or (dp[x][y+length-k][k] and dp[x+k][y][length-k])
        return dp[0][0][n]
if __name__ == "__main__":
    s = Solution1()
    s1 = "abcd"
    s2 = "badc"

    print s.isScramble( s1, s2)