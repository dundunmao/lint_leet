# -*- encoding: utf-8 -*-
# eg:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# 同题 Strobogrammatic Number 

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        str = str.split()
        if len(pattern) != len(str):
            return False

        if len(set(pattern)) != len(set(str)):  #这个要检查否则s="ab",t="aa"会return True
            return False
        le = len(pattern)
        i,j = 0,0
        hash = {}
        while i < le and j < le:
            if hash.has_key(pattern[i]):
                if hash[pattern[i]] != str[j]:
                    return False
            else:
                hash[pattern[i]] = str[j]
            i += 1
            j += 1
        return True
if __name__ == '__main__':
    a = "abba"
    b = "dog cat cat dog"
    s = Solution()
    print s.wordPattern(a,b)