# -*- encoding: utf-8 -*-
# 给定一个有向图，图节点的拓扑排序被定义为：
#
# 对于每条有向边A--> B，则A必须排在B之前　　
# 拓扑排序的第一个节点可以是任何在图中没有其他节点指向它的节点　　
# 找到给定图的任一拓扑排序
#
#
#
#  注意事项
#
# 你可以假设图中至少存在一种拓扑排序
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# Learn more about representation of graphs
#
# 样例
# 对于下列图：
#
#
#
# 这个图的拓扑排序可能是：
#
# [0, 1, 2, 3, 4, 5]
#
# 或者
#
# [0, 2, 3, 1, 5, 4]
from Queue import Queue
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        result = []
        hash = {}
        for x in graph:
            hash[x] = 0

        for i in graph:
            for j in i.neighbors:
                hash[j] += 1
        q = Queue()

        for node2 in graph:
            if hash[node2] == 0:
                q.put(node2)
                result.append(node2)
        while not q.empty():
            node3 = q.get()
            for n in node3.neighbors:
                hash[n] = hash.get(n) - 1
                if hash.get(n) == 0:
                    result.append(n)
                    q.put(n)
        return result
