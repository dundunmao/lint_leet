# -*- encoding: utf-8 -*-
#2级
# 内容：两个string是不是变位词("anagram"和 "nagaram",是；"rat"和"car"不是)
# 思路：sorted(string)
#Time Limit Exceeded
# def isAnagram(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     s = list(s)
#     t = list(t)
#     if len(s) != len(t):
#         return False
#     for i in range(0, len(s)):
#         for j in range(0,len(t)):
#             if s[i] == t[j]:
#                 t.remove(t[j])
#                 break
#     if t == []:
#         return True
#     else:
#         return False


class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        return s == t