class ConnectingGraph3:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.root = [0 for _ in xrange(n + 1)]
        self.count = n

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
            self.count -= 1

    # @param {int} a
    # return {int} the number of connected component
    # in the graph
    def query(self):
        # Write your code here
        return self.count