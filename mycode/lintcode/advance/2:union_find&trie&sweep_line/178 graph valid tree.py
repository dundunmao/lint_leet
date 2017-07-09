class union_find:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.root = [i for i in range(n)]

    def find(self, x):
        if self.root[x] == x:
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

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if n - 1 != len(edges):
            return False
        uf = union_find(n)
        for i in range(len(edges)):
            root1 = uf.find(edges[i][0])
            root2 = uf.find(edges[i][1])
            if root1 == root2:
                return False
            else:
                uf.connect(edges[i][0],edges[i][1])
        return True

if __name__ == '__main__':
    n = 5

    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    s = Solution()
    print s.validTree(n, edges)