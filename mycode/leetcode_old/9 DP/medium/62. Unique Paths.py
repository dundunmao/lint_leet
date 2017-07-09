# coding:utf-8
# 题目: 走格子,从左上角走到右下角,方向只能是右和下.问有多少条路可走
# 思路
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        aux = [[1 for x in range(n)] for x in range(m)] #先设除第一趟,其他格子里都为1
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]  #每个格子里的数都是它的上格子和左格子里数的和.每个格子里的数为走到他这有多少条路
        return aux[-1][-1]