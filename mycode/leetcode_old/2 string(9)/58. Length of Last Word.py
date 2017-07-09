# -*- encoding: utf-8 -*-
# 1级
# 题目：例如Given s = "Hello World",return 5。最后一个word的长度
# 思路：用s.split
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        if len(l) == 0:
            return 0
        else:
            return len(l[-1])