# -*- encoding: utf-8 -*-
# 克隆一张无向图，图中的每个节点包含一个 label 和一个列表 neighbors。
#
# 数据中如何表示一个无向图？http://www.lintcode.com/help/graph/
#
# 你的程序需要返回一个经过深度拷贝的新图。这个新图和原图具有同样的结构，并且对新图的任何改动不会对原图造成任何影响。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如，序列化图 {0,1,2#1,2#2,2} 共有三个节点, 因此包含两个个分隔符#。
#
# 第一个节点label为0，存在边从节点0链接到节点1和节点2
# 第二个节点label为1，存在边从节点1连接到节点2
# 第三个节点label为2，存在边从节点2连接到节点2(本身),从而形成自环。
# 我们能看到如下的图：
#
#    1
#   / \
#  /   \
# 0 --- 2
#      / \
#      \_/
from Queue import Queue
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return node
        # 用BFS来traverse图并得到所以nodes
        nodes = self.getNodes(node)

        # copy nodes, 存hash(key->value = old node->new node)
        hash = self.dict
        for each1 in nodes:
            hash[each1] = UndirectedGraphNode(each1.label)

        # copy neighbors
        for each2 in nodes:
            new_node = hash.get(each2)
            for neighbor in each2.neighbors:
                new_neighbor = hash.get(neighbor)
                new_node.neighbors.append(new_neighbor)
        return hash.get(node)


    def getNodes(self,node):
        queue = Queue()
        set = {}
        queue.put(node)
        set[node] = True
        while not queue.empty():
            head = queue.get()
            for neighbor in head.neighbors:
                if not set.has_key(neighbor):
                    set[neighbor] = True
                    queue.put(neighbor)
        return set
