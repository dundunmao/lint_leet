# -*- encoding: utf-8 -*-
#2级
# 题目：同构，例如"egg", "add"；"paper", "title"
# 思路：用dictionary，第一个词作为key,第二个词作为value，
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:    #key不存在
                if t[i] in dict.values():    #value存在
                    return False
                dict[s[i]] = t[i]   #创建key value pair
            else:
                if dict[s[i]] != t[i]:  #如果key存在但是value对不上，false
                    return False
        return True