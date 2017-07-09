# -*- encoding: utf-8 -*-
# 假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。设计一个算法来找到最大的利润。你最多可以完成两笔交易。
#
#  注意事项
#
# 你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一个样例数组 [4,4,6,1,1,4,2,5], 返回 6
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if prices is None or len(prices) == 0:
            return 0
        left = [0]*len(prices)
        right = [0]*len(prices)
        min_price_left = float('inf')
        max_price_right = float('-inf')
        max_profit_left = 0
        max_profit_right = 0
        for i in range(len(prices)):
            min_price_left = min(min_price_left, prices[i])
            max_profit_left = max(max_profit_left, prices[i]-min_price_left)
            left[i] = max_profit_left
        for j in range(len(prices))[::-1]:
            max_price_right = max(max_price_right, prices[j])   #这里注意,从后往前遍历,每次找的是最大price
            max_profit_right = max(max_profit_right, max_price_right - prices[j])
            right[j] = max_profit_right
        max_two = float('-inf')
        for k in range(len(prices)):
            max_two = max(max_two, left[k]+right[k])
        return max_two


# 我的练习
# 跟上面一样的
class Solution1:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if prices is None or len(prices) == 0:
            return 0
        if len(prices) == 1:
            return 0
        # one transaction
        max_one = self.helper(prices)[-1]
        # max_one = max_one_array[-1]
        # two transaction
        # from left to right
        max_two = 0
        max_two_left = self.helper(prices)
        # from right to left
        max_two_right = self.helper_reverse(prices[::-1])
        # sum
        for i in range(len(max_two_left)-1):
            max_two = max(max_two,max_two_left[i]+max_two_right[-i-2])
        return max(max_one,max_two)
    def helper(self, prices):
        # initialize
        le = len(prices)
        min_prices = prices[0]
        max_pro = 0
        max_array = [0]
        # for loop
        for i in range(1,le):
            min_prices = min(min_prices, prices[i])
            max_pro = max(max_pro, prices[i] - min_prices)
            max_array.append(max_pro)
        return max_array
    def helper_reverse(self, prices):
        le = len(prices)
        max_prices = prices[0]
        max_pro = 0
        max_array = [0]
        # for loop
        for i in range(1,le):
            max_prices = max(max_prices, prices[i])
            max_pro = max(max_pro, max_prices - prices[i])
            max_array.append(max_pro)
        return max_array

if __name__ == "__main__":

    A = [3,2,6,5,0,3]

    s = Solution1()

    print s.maxProfit(A)