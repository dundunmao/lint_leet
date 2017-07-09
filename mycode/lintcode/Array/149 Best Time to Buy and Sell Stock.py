# -*- encoding: utf-8 -*-
# 假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一个数组样例 [3,2,3,1,2], 返回 1
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
# 用max subarray的方法
    def maxProfit(self, prices):
        # write your code here
        if prices is None or len(prices) == 0:
            return 0
        B = []
        for i in range(1, len(prices)):
            B.append(prices[i]-prices[i-1])
        pre_sum_i = 0
        max_sum = 0  # 这题唯一跟max subarray不同的是这里是0,不是负无穷
        min_sum = 0
        for i in range(len(B)):
            pre_sum_i += B[i]
            max_sum = max(max_sum, pre_sum_i-min_sum)
            min_sum = min(min_sum, pre_sum_i)
        return max_sum
# 这个方法可用**
# 每次记录最小的price和最大的profit

    def maxProfit_leet(self, prices):
        if prices is None or len(prices) == 0:
            return 0
        mini = prices[0]
        result = 0
        for i in range(len(prices)):
            now = prices[i] - mini #在前面最低的一次买，当前次卖，得到的最新收益
            result = max(result, now)  #最新收益跟之前最好收益取最大
            mini = min(mini,prices[i])  #更新最低价
        return result


# 我的练习
#++================================================
# 1: brute force; time limit exceeded
class Solution1:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if prices is None or len(prices) == 0:
            return 0
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                max_profit = max(max_profit, prices[j]-prices[i])
        return max_profit

# ============================================
# 这个方法可用 **
#  遍历一个flag.用flag后的最大element 减去 flag前的最小element.
# 第一个for loop 得到每个前缀的最小值,得到一个array. 第二个for loop 取每个后缀的最大值,得到一个array
# 第三个for loop 让前两个array对应项互减.
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if prices is None or len(prices) == 0:
            return 0
        # min element in prefix
        mini_prefix = [prices[0]]
        mini = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            mini_prefix.append(mini)
        # maxi elemt in postfix
        maxi_postfix = [prices[-1]]
        maxi = prices[-1]
        for i in range(len(prices)-2, 0, -1):
            if prices[i] > maxi:
                maxi = prices[i]
            maxi_postfix.append(maxi)
        max_profit = 0
        for i in range(0, len(prices)-1):
            max_profit = max(max_profit,maxi_postfix[len(prices)-i-2]-mini_prefix[i])
        return max_profit

if __name__ == "__main__":

    A = [3,2,6,5,0,3]
    s = Solution()

    print s.maxProfit(A)