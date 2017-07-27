# -*- encoding: utf-8 -*-
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# 给一个只有A，L，P，的string，如果有一个以上的A或两个以上的连续L，就是False
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for str in s:
            if str == "A":
                a += 1
            if str == 'L':
                l += 1
            else:
                l = 0
            if l > 2 or a > 1:
                return False
        return True
