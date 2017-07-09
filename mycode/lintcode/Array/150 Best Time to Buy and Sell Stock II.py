# -*- encoding: utf-8 -*-
# 假设有一个数组，它的第i个元素是一个给定的股票在第i天的价格。设计一个算法来找到最大的利润。你可以完成尽可能多的交易(多次买卖股票)。然而,你不能同时参与多个交易(你必须在再次购买前出售股票)。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一个数组样例[2,1,2,0,1], 返回 2
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        B = []
        profit = 0
        for i in range(1,len(prices)):
            b = prices[i]-prices[i-1]
            if b > 0:
                profit += b
        return profit

# 我的练习
class Solution2:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        # edge case:
        if prices is None or len(prices) == 0:
            return 0

        le = len(prices)
        profit = []
        for i in range(1,le):
            profit.append(prices[i] - prices[i-1])
        max_profit = 0
        for i in range(len(profit)):
            if profit[i]>0:
                max_profit += profit[i]
        return max_profit


