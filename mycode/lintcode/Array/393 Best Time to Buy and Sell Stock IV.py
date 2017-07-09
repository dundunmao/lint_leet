# -*- encoding: utf-8 -*-
# 假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
#
# 设计一个算法来找到最大的利润。你最多可以完成 k 笔交易。
#
#  注意事项
#
# 你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给定价格 = [4,4,6,1,1,4,2,5], 且 k = 2, 返回 6.
class Solution:
    """
    @param k: an integer
    @param prices: an integer array
    @return: an integer which is maximum profit
    """
    def maxProfit(self, k, prices):
        # write your code here
        if k == 0:
            return 0
        if k >= len(prices)/2: #如果交易次数多余(天数的一半)就相当于 (ii)那道题
            profit = 0
            for i in range(1,len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        n = len(prices)
        # 第i天正好完成第j笔交易的最大收益作为局部变量local。
        local_profit = [[0 for i in range(k+1)] for j in range(n)]
        # 第i天已经执行j笔交易的最大收益作为全局变量global
        global_profit = [[0 for i in range(k+1)] for j in range(n)]

        for i in range(1, n):
            diff = prices[i] - prices[i-1]

            for j in range(1, k+1):
                # 对于local(第i天正好完成第j笔交易的最大收益)，可以基于第i-1天正好完成第j-1笔交易的最大收益加上当天交易的差值，还有第i-1天正好完成第j笔交易的最大收益加上当天交易的差值。
                # 要注意的是，第i-1天正好完成第j-1笔交易这种情况，当前交易的差值取0和实际昨天今天差价中较大的，因为我们还有一次自由交易的余地，所以如果亏的话完全可以当天买卖避免损失。
                # 但第i-1天正好完成第j笔交易这种情况来推导第i天正好完成第j笔交易时，相当于第i天已经要连着第i-1天交易，使得第i - 1天正好完成的第j笔交易和第i天正好完成的第j笔交易是同一个交易。

                local_profit[i][j] = max(global_profit[i-1][j-1]+max(0, diff), local_profit[i-1][j]+diff)
                # 对于global:第i天已经执行j笔交易的最大收益，可以基于第i - 1天已经执行j笔交易的最大收益和第i天正好完成第j笔交易的最大收益
                global_profit[i][j] = max(global_profit[(i - 1)][j], local_profit[i][j])
        return global_profit[(n - 1)][k]


class Solution_leet:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        最多k次交易
        """
        if prices is None or len(prices) == 0:
            return 0
        l = len(prices)
        profit = 0
        if k >= l / 2:
            for i in range(1, l):
                diff = prices[i] - prices[i-1]
                if diff > 0:
                    profit += diff
            return profit
        loc = [[0 for j in range(k + 1)] for i in range(l)]
        glo = [[0 for j in range(k + 1)] for i in range(l)]

        for i in range(1, l):
            diff = prices[i] - prices[i-1]
            for j in range(1, k + 1):
                loc[i][j] = max(loc[i - 1][j]+diff,
                                glo[i - 1][j - 1] + max(0,diff))
                glo[i][j] = max(glo[i - 1][j],
                                loc[i][j])
        return glo[l - 1][k]
if __name__ == "__main__":

    A = [2,3,5,4,6,20]
    k = 2
    s = Solution_leet()

    print s.maxProfit(k,A)
