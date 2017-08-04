# coding:utf-8
# 实现一个数据结构，提供下面两个接口
# 1.add(number) 添加一个元素
# 2.topk() 返回前K大的数
# http://www.jiuzhang.com/solutions/top-k-largest-number-ii
# 样例
# s = new Solution(3);
# >> create a new data structure.
# s.add(3)
# s.add(10)
# s.topk()
# >> return [10, 3]
# s.add(1000)
# s.add(-99)
# s.topk()
# >> return [1000, 10, 3]
# s.add(4)
# s.topk()
# >> return [1000, 10, 4]
# s.add(100)
# s.topk()
# >> return [1000, 100, 10]
# 这题要一直保持数组的各数小于等于K。
from heapq import *


class Solution:
    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.nums = []
        self.k = k
        heapify(self.nums)

    # @param {int} num an integer
    def add(self, num):
        # Write your code here
        if len(self.nums) < self.k:
            heappush(self.nums, num)
        elif num > self.nums[0]:
            heappop(self.nums)
            heappush(self.nums, num)

    # @return {int[]} the top k largest numbers
    def topk(self):
        # Write your code here
        return sorted(self.nums, reverse=True)
