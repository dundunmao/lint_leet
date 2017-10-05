# coding:utf-8
#  Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
# Return -1 if knight can not reached.
#
#  注意事项
#
# source and destination must be empty.
# Knight can not enter the barrier.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# If the knight is at (x, y), he can get to the following positions in one step:
#
# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)
# 样例
# [[0,0,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 2
#
# [[0,1,0],
#  [0,0,0],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return 6
#
# [[0,1,0],
#  [0,0,1],
#  [0,0,0]]
# source = [2, 0] destination = [2, 2] return -1

# Definition for a point.

# BFs+hash
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from collections import deque
class Solution:
    """
    @param: grid: a chessboard included 0 (false) and 1 (true)
    @param: source: a point
    @param: destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if grid == [] or grid == [[]]:
            return 0
        q = deque()
        hash = {}
        q.append([source,0])
        row = len(grid)
        col = len(grid[0])
        coordination = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
        while len(q) != 0:
            node = q.popleft()
            for x,y in coordination:
                new_node = Point(node[0].x+x, node[0].y+y)
                if (new_node.x,new_node.y) in hash:
                    continue
                elif new_node.x < row and new_node.x > -1 and new_node.y < col and new_node.y > -1 and grid[new_node.x][new_node.y] == 0:
                    if new_node.x == destination.x and new_node.y == destination.y:
                        return node[1]+1
                    hash[(new_node.x,new_node.y)] =  node[1]+1
                    q.append([new_node,node[1]+1])

        return -1

if __name__ == "__main__":





    A = [[0,0,0],[0,0,0],[0,0,0]]
    B = Point(2,0)
    C = Point(2,2)
    hash = {}
    hash[B] = 0
    s = Solution()

    print s.shortestPath(A,B,C)