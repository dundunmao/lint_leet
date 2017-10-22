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
from collections import deque
from Queue import Queue
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
# in-degree & out-degree法
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        result = []
        hash = {}
        # 把每个点加入hash里，value的in-dgree
        for x in graph:
            hash[x] = 0
        # 把每个点的in-degree算出来
        for i in graph:
            for j in i.neighbors:
                hash[j] += 1
        # BFS，先把所有in-degree为0的放queue里，并把他们都append到result里。
        q = deque()

        for node2 in graph:
            if hash[node2] == 0:
                q.append(node2)
                result.append(node2)
        # 然后没popleft一个node，就把他们的邻居的in-degree 减1，边减边看in-degree是0，就加入queue和result里
        while len(q) != 0:
            node3 = q.popleft()
            for n in node3.neighbors:
                hash[n] -= 1
                if hash[n] == 0:
                    result.append(n)
                    q.append(n)

        return result


