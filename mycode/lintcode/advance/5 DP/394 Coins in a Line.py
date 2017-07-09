# -*- encoding: utf-8 -*-
#  题目:有 n 个不同价值的硬币排成一条线。两个参赛者轮流从左边依次拿走 1 或 2 个硬币，直到没有硬币为止。计算两个人分别拿到的硬币总价值，价值高的人获胜。
#        请判定第一个玩家是输还是赢？
# eg: 给定数组A = [1, 2, 2], 返回true.A = [1, 2, 4], 返回false.


class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        f = [None for i in range(n+1)]
        # flag = [None for i in range(n+1)]
        if n == 0 or n == 3:
            return False
        elif n == 1 or n == 2:
            return True
        f[0] = False
        f[1] = True
        f[2] = True
        f[3] = False

        for i in range(4, n + 1):
            f[i] = (f[i - 2] and f[i - 3]) or (f[i - 4] and f[i - 3])
        return f[n]
class Solution1:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        f = [None for i in range(n+1)]
        if n == 0:
            return False
        elif n == 1 or n == 2:
            return True
        f[0] = False
        f[1] = True
        f[2] = True
        for i in range(3, n + 1):
            if f[i-1] is False or f[i-2] is False:
                f[i] = True
            else:
                f[i] = False
        return f[n]

if __name__ == "__main__":
    s = Solution1()
    n = 4
    print s.firstWillWin(n)