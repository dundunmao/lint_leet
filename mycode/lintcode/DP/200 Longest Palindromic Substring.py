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





if __name__ == "__main__":
    x = "aaaabaaa"
    s = Solution1()
    print s.longestPalindrome(x)
            