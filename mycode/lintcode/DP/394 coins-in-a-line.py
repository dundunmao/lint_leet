# coding:utf-8
# 有 n 个硬币排成一条线。两个参赛者轮流从右边依次拿走 1 或 2 个硬币，直到没有硬币为止。拿到最后一枚硬币的人获胜。
#
# 请判定 第一个玩家 是输还是赢？
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# n = 1, 返回 true.
#
# n = 2, 返回 true.
#
# n = 3, 返回 false.
#
# n = 4, 返回 true.
#
# n = 5, 返回 true.

class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        dp = [None for i in range(n+1)]
        flag = [None for i in range(n+1)]
        return self.search(n,dp,flag)
    def search(self,n,dp,flag):
        if n == 0:
            return False
        if n == 1:
            return True
        if n == 2:
            return True
        if n == 3:
            return False
        flag[n] = True
        dp[n] = (self.search(n-2,dp,flag) and self.search(n-3,dp,flag)) or (self.search(n-3,dp,flag) and self.search(n-4,dp,flag))
        return dp[n]

class Solution1:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        dp = [None for i in range(n+1)]
        # flag = [None for i in range(n+1)]
        if n == 0 or n == 3:
            return False
        elif n == 1 or n == 2:
            return True
        dp[0] = False
        dp[1] = True
        dp[2] = True
        dp[3] = False

        for i in range(4, n + 1):
            dp[i] = (dp[i - 2] and dp[i - 3]) or (dp[i - 4] and dp[i - 3])

        return dp[n]




if __name__ == "__main__":

    s = Solution1()
    print s.firstWillWin(1)