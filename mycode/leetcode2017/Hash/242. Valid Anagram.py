# -*- encoding: utf-8 -*-
# 相同字母异序词
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        相同字母异序词
        """
        if len(s) == 0 and len(t) == 0:
            return True
        if len(s) != len(t):
            return False
        hash = {}
        for str in s:
            if hash.has_key(str):
                hash[str] += 1
            else:
                hash[str] = 1
        for str in t:
            if not hash.has_key(str):
                return False
            else:
                hash[str] -= 1
        for v in hash.values():
            if v != 0:
                return False