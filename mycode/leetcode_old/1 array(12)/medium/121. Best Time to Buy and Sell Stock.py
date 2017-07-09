# coding:utf-8
#题目:有一个list,第i个element是第i天的股票价值.你只被运行进行一次交易(买一次卖一次),求算法得到最大利益(maximum profit)
#思路,假设我有sum钱,profit=(sum/list[i]*list[j]-sum) = sum(list[j]/list[i]-1)要这个数最大
# 其实就是要(list[j]/list[i])最大,且j>i
# 从后往前遍历,先记录从后往前遇到的最大的数,接着记录最大的数和目前这个数的最大的差
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length==0:
            return 0
        temp = prices[length-1]
        res = 0
        for i in range(length-1,-1,-1):
            temp = max(temp,prices[i])   #记录从后往前遇到的最大的数
            if temp - prices[i] > res:
                res = temp - prices[i]   #记录最大的数和目前这个数的最大的差
        return res

if __name__ == '__main__':
    prices = [2,5,7,4,6,2]
    s = Solution()
    print s.maxProfit(prices)