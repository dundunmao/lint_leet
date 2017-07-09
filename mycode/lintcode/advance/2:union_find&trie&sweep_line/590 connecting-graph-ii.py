class ConnectingGraph2:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.root = [0 for _ in xrange(n + 1)]
        self.size = [1 for _ in xrange(n + 1)]

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
            self.size[root_b] += self.size[root_a]

    # @param {int} a
    # return {int}  the number of nodes connected component
    # which include a node.
    def query(self, a):
        # Write your code here
        root_a = self.find(a)
        return self.size[root_a]
