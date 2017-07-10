# -*- encoding: utf-8 -*-
# 同构
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):  #这个要检查否则s="ab",t="aa"会return True
            return False
        le = len(s)
        i,j = 0,0
        hash1 = {}
        while i < le and j < le:
            if hash1.has_key(s[i]):
                if hash1[s[i]] != t[j]:
                    return False
            else:
                hash1[s[i]] = t[j]
            i += 1
            j += 1
        return True

if __name__ == '__main__':
    a = "egg"
    b = "add"
    s = Solution()
    print s.isIsomorphic(a,b)