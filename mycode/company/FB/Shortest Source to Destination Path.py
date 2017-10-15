# -*- encoding: utf-8 -*-
from collections import deque
# start = [i,j]
# end = [i',j']
def short_path(matrix,start,end):
    q = deque()
    q.append(start)
    res = 0
    coordination = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    # coordination/ = [[1,0],[-1,0],[0,1],[0,-1]]
    hash = {}
    while q:
        le = len(q)
        for i in range(le):
            cur = q.pop()
            if cur == end:
                return res
            else:
                #check four direction and append in q
                i = cur[0]
                j = cur[1]
                for k in coordination:
                    new_i = k[0]
                    new_j = k[-1]
                    if new_i>=0 and new_j>=0 and new_i < len(matrix) and new_j < len(matrix[0]) and matrix[i][j-1] == 0 and (new_i,new_j) not in hash:
                        q.append((new_i,new_j))
                        hash[(new_i,new_j)] = True
                res += 1
    return -1