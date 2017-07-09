# coding:utf-8
#题目:有一个list,第i个element是第i天的股票价值,求算法得到最大利益(maximum profit).你只被运行进行多次交易(但是必须买到了之后才能卖)
#思路:



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

if __name__ == '__main__':
    prices = [1,2,3,4,4,4]
    s = Solution()
    print s.maxProfit(prices)