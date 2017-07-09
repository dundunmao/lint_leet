# -*- encoding: utf-8 -*-

# 题目；设计一个stack，可以push,pop,top和得到里面最小的元素
# 思路：stack的每一个element由两个数组成（刚压入的数，现在最小的数）
# 关键语句：
class MinStack:

    def __init__(self):
        self.q = []             #是一个（每一个element由两个数组成)的list
    def push(self, x):
        curMin = self.getMin()         #最小那个数
        if curMin == None or x < curMin:             #如果刚压入的数x比之前里面最小的数curMin小，那x就变成最小的数curMin
            curMin = x
        self.q.append((x, curMin))              #增加一个element (x, curMin)
    def pop(self):   # @return nothing
        self.q.pop()
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]   #最后面那个element里的第一个数
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]    #最后面那个element的第二个数
