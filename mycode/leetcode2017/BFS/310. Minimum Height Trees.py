# -*- encoding: utf-8 -*-
# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
#
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).
#
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#
# Example 1:
#
# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#         0
#         |
#         1
#        / \
#       2   3
# return [1]
#
# Example 2:
#
# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]
#
# Note:
#
# (1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
#
# (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
import collections
from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return[0]
        # 建立hash，key为node.v,value为node.neighor.这里不把他变成 class undirectGraph的实例，只用value就好
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)   #261. Graph Valid Tree也是这样做的，对于每一个边【a,b】把a加入b的edge里，把b加入a的edge里。
            graph[v].append(u)

        res = []
        # for every node, BFS, recode the height
        for node in graph:        #对于每一个node做BFS
            visit = {node:True}   #新建visit
            q = deque()           #新建deque
            q.append(node)
            count = -1
            while len(q) != 0:     #开始以node为起点，层层遍历，并记住是第几层
                number = len(q)
                for i in range(number):
                    cur = q.popleft()
                    for neighbor in graph[cur]:
                        if not visit.has_key(neighbor):
                            visit[neighbor] = True
                            q.append(neighbor)
                count += 1
            res.append([count,node])
        ans = sorted(res,key = lambda x:x[0])
        return [y for x,y in ans if x == ans[0][0]]


import collections
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        graph=collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        # 把所以degree为1（就是edge里面只有一个node的）的加入leaves，
        leaves = [i for i in xrange(n) if len(graph[i]) == 1]

        while n > 2: #当n还是两个点时，说明相遇了
            n -= len(leaves) #每次从n里减去叶子的各数
            newLeaves = []
            # 对于里面的每个点i，都找到跟他相连的那个点j，然后把这个点i从j的edge里删掉，相当于把j的degree减一。
            for i in leaves:
                j = graph[i].pop()  #j就跟这个叶子相连的那个node
                graph[j].remove(i)  #减j的degree
                if len(graph[j]) == 1:   #如果degree为1了，就加入leaves
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves
if __name__ == '__main__':
    a = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    b = 6
    s = Solution()
    print s.findMinHeightTrees(b,a)
