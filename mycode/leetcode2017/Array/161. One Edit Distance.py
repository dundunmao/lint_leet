# -*- encoding: utf-8 -*-
# Given two strings S and T, determine if they are both one edit distance apart.
#
# Given s = "aDb", t = "adb"
# return true

 # * There're 3 possibilities to satisfy one edit distance apart:
 # *
 # * 1) Replace 1 char:
 # 	  s: a B c
 # 	  t: a D c
 # * 2) Delete 1 char from s:
	#   s: a D  b c
	#   t: a    b c
 # * 3) Delete 1 char from t
	#   s: a   b c
	#   t: a D b c
 # */
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return self.isOneEditDistance(t,s)  #让长的永远是后面这个
        diff = len(t)-len(s)
        if diff > 1:  #两个长度相差大于1时，肯定false
            return False
        if diff == 0:   #两个长度相同时，只有一个被替换
            count = 0
            for i in range(0,len(s)):
                if t[i] != s[i]:
                    count += 1
            return count==1
        if diff == 1:    #t比s多出一位时，检查有任何一位不同，就那t的那位扔掉，
            for i in range(0,len(s)):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
        return True  #处理最后s='',t='c',for循环跳出的情况
if __name__ == '__main__':
    a = "a"
    t = "ah"
    s = Solution()
    print s.isOneEditDistance(a,t)


















