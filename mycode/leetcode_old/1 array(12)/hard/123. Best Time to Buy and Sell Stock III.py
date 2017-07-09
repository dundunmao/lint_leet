# -*- encoding: utf-8 -*-
# 3级
# 内容:list里第i个element是第i天的股票值,算出最大profit.条件是一次只能hold一个股票,最多进行两次交易.就是说第一次交易完成后才能进行第二次交易
# 思路:假设我有sum钱,profit=(sum/list[i]*list[j]-sum) = sum(list[j]/list[i]-1)要这个数最大,求(list[j]/list[i]-1)最大,这是一次交易.
# 找正走最大差,反走最大差,但是两个不能相交
# 也就是在0<= i <= length-1 这个位置,左边最大,右边最大.然后不断更新profit.

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = [0]*len(prices)
    low, high = float('inf'), float('-inf')    #正无穷大和负无穷大
    max_profit = res = 0
    for n, p in enumerate(prices):          #遍历prices
        low = min(p, low)                  #记录最小price
        diff_left = p-low                  #记录最大差
        max_profit = max(max_profit,diff_left )   #这轮的最大差和原来的最大差取max
        profit[n] = max_profit               #在这天之前的profit,也就是在i这个位置的profit就是这个最大差
    max_profit = 0
    for n, p in reversed(list(enumerate(prices))):   #从后往前遍历
        high = max(p, high)                          #记录最大price
        diff_right= high-p                          #记录最大差
        max_profit = max(max_profit, diff_right)     #这轮的最大差和原来的最大差取max
        res = max(res, max_profit+profit[n])         #从前往后和从后往前的最大差在这个点上的和,取最大
    return res
if __name__ =="__main__":
    prices = [2,5,7,4,6,2]
    print maxProfit(prices)