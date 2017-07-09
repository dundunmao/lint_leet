# 0级
# -*- encoding: utf-8 -*-
# 内容：给一叠石头,两个人玩,每次只能移走1,2,3块,
# 思路：如果你最后留下的石头是1,2,3块,那对方就赢 所以就看能不能被4整除

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)