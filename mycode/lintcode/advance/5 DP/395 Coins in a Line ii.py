# -*- encoding: utf-8 -*-
# 方法一从先手角度出发
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    # def firstWillWin(self, values):
    def firstWillWin(self, values):
        n = len(values)
        f = [0 for i in range(n+1)]
        sum = 0
        for v in values:
            sum += v
        f[0] = 0
        if n > 0:
            f[1] = values[n-1]
        if n > 1:
            f[2] = values[n-1] + values[n-2]
        if n > 2:
            f[3] = values[n-2] + values[n-3]

        if n>3:
            for i in range(4,n+1):
                f[i] = max(
                min(f[i-2], f[i-3]) + values[n - i],
                min(f[i-3], f[i-4]) + values[n - i] + values[n - i + 1])
        return sum < 2 * f[n]
#方法一的九章模式
class Solution1:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # n = len(values)
        f = [0 for i in range(len(values)+1)]
        flag = [0 for i in range(len(values) + 1)]
        sum = 0
        for v in values:
            sum += v
        return sum < 2*self.helper(len(values), f, flag, values)
    def helper(self, n, f, flag, values):
        if flag[n] is True:
            return f[n]
        flag[n] = True
        if n == 0:
            f[n] = 0
        elif n == 1:
            f[n] = values[len(values)-1]
        elif n == 2:
            f[n] = values[len(values)-1] + values[len(values)-2]
        elif n == 3:
            f[n] = values[len(values)-2] + values[len(values)-3]
        else:
            f[n] = max(
                min(self.helper(n - 2, f, flag, values), self.helper(n - 3, f, flag, values)) + values[len(values) - n],
                min(self.helper(n - 3, f, flag, values), self.helper(n - 4, f, flag, values)) + values[
                    len(values) - n] + values[len(values) - n + 1])
        return f[n]
# 方法二:从当前人角度出发
class Solution2:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        f = [0 for i in range(n+1)]
        sum = 0
        for v in values:
            sum += v
        f[1] = values[n-1]
        for i in range(2,n+1):
            f[i] = max(sum[i]-f[i-1], sum[i]-f[i-2])
        return f[n]>sum[n]/2


if __name__ == "__main__":
    s = Solution2()
    A = [1,2,4,8]
    print s.firstWillWin(A)

