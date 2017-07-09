# -*- encoding: utf-8 -*-
# 给n个nodes, labeled from 1 to n,开始没有edges.
# 需要support如下方法:
# 1:connect(a, b)把a,b连上
# 2:query(a,b)检查两点是否链接上

#5 // n = 5
# query(1, 2)
# return false
# connect(1, 2)
# query(1, 3)
# return false
# connect(2, 4)
# query(1, 4)
# return true


class ConnectingGraph:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.root = [0 for i in range(n + 1)]

    def find(self, x):
        if self.root[x] == 0:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.root[root_a] = root_b

    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b