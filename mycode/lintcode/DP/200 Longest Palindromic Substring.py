# coding:utf-8
# 给出一个字符串（假设长度最长为1000），求出它的最长回文子串，你可以假定只有一个满足条件的最长回文串。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出字符串 "abcdzdcab"，它的最长回文子串为 "cdzdc"。

class Solution1(object):
    def longestPalindrome(self, s):


        f = [(s[i],1) for i in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(0,i):
                if self.pali(s[j:i+1]):
                    f[i] = (s[j:i+1],i+1-j)
                    break
        sort_f = sorted(f,key = lambda x:x[1])
        return sort_f[-1][0]

    def pali(self,x):
        i = 0
        j = len(x)-1
        while i<j:
            if x[i] != x[j]:
                return False
            else:
                i += 1
                j -= 1
        return True


class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ()
        f = [[False for i in range(n)] for j in range(n)]  # 代表（i-j）这块的substring是不是palin
        for i in range(n - 1, -1, -1):  # 从后往前走是因为f[i][j]是从f[i+1][j-1]得到的，要先知道后面的才行。
            for j in range(i, n):
                # j-i<3代表（char自己）&（两个挨着的char）& （俩char中间有个char）->取决两个数相等不。
                # 不写这句会越界
                if j - i < 3 or f[i + 1][j - 1]:  # ，f[i+1][j-1]就表示两边向外扩一位。
                    f[i][j] = s[i] == s[j]
                if f[i][j] and (res == () or j - i + 1 > res[1] - res[0]):
                    # res = s[i:j+1]  不直接给substring而是记录始终点，因为s[i:j]是time killer
                    res = (i, j + 1)
        return s[res[0]:res[1]]



if __name__ == "__main__":
    x = "aaaabaaa"
    s = Solution1()
    print s.longestPalindrome(x)
            