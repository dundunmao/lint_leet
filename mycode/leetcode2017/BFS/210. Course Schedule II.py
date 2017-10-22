# -*- encoding: utf-8 -*-
# 给n门课，一些课是另一些的前置课，
# For example:
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
# 问上课的顺序
# 这题基本上就是lintcode：/topological-sorting/那道题，一模一样
class Graph_node():
    def __init__(self,x):
        self.v = x
        self.neighbors = []

from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        graph = []
        #创建graph node,放hash的key里
        for i in range(numCourses):
            graph.append(Graph_node(i))
        #把neighbors加进去
        for i in range(numCourses):
            for ele in prerequisites:
                if ele[1] == graph[i].v:
                    graph[i].neighbors.append(graph[ele[0]])
        # 创建in-degree的hash
        hash = {}
        for node in graph:
            hash[node] = 0
        # 把每个node的in-degree算出来
        for node in hash:
            for nerbor in node.neighbors:  #一旦发现某个node是属于edge的，他的in-degree就加一。
                hash[nerbor] += 1

        # BFS
        q = deque()
        #先把in-degree为0的都加入queue里，也放入res里
        for node in hash:
            if hash[node] == 0:
                q.append(node)
                res.append(node.v)
        # 开始pop,每pop一个，就把他的每一个邻居的in-degree -1，如果邻居的in-degree为0了，就让入queue和res里
        while len(q) != 0:
            node = q.popleft()
            for ele in node.neighbors:
                hash[ele] -= 1
                if hash[ele] == 0:
                    res.append(ele.v)
                    q.append(ele)
        # 如果并没有把所以的node都存入res，说明有环，这种情况就return 【】
        if len(res) != numCourses:
            return []
        return res

if __name__ == "__main__":
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]

    prerequisites =[[1, 0], [2, 1], [3, 2], [1, 3]] #有环
    numCourses = 4
    s = Solution()
    print s.findOrder(numCourses, prerequisites)
