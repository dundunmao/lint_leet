# -*- encoding: utf-8 -*-

class MergeEmailList():
    def merge(self,emails):
        res = []
        if emails == None or len(emails) == 0:
            return res
        m = len(emails)
        parent = [i for i in range(m)]
        map = {}
        # map 是email为key。A1,A1的array为value的
        for A in emails:  #对于emails里的每一个account A1,A2。。
            for e in emails[A]:  #对于每一个A1下面的email列表，e是其中个email
                if map.has_key(e):
                    map[e].append(A)
                else:
                    map[e] = [A]
        for A in map.values():
            for i in range(len(A)):
                self.union(parent,A[0],A[i])




    def union(self, parent,x,y):
        parentX = self.getParent(parent,x)
        parentY = self.getParent(parent,y)
        if parentX < parentY:
            parent[parentY] = parentX
        elif parentX > parentY:
            parent[parentX] = parentY

    def getParent(self,parent,x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

if __name__ == '__main__':
    emails = {'A1': ['a1', 'a2'], 'A2': ['b1', 'a2'], 'A3': ['c1'], 'A4': ['c1', 'd1'], 'A5': ['b1', 'e1']}
    s = MergeEmailList()
    print s.merge(emails)

