# -*- encoding: utf-8 -*-
# 每加入一个岛屿,集合个数加一,每合并一次集合个数建议


class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def __init__(self):
        self.root = []

    def find(self, x):   #找root
        if self.root[x] == x:  #如果这个位置的数就是他的下标,这个下标就是root
            return x
        self.root[x] = self.find(self.root[x])  #x这个下标上的数=以这个数为下标的那个位置的数
        return self.root[x]

    def merge(self, x, y): #能否合并,如果能就把x位置的值标记成y,意思是x的root是y.
        if self.root[x] == -1 or self.root[y] == -1:   #如果其中有一个是-1,就false
            return False

        x = self.find(x)  #找到x的根.
        y = self.find(y)  #找到y的根
        if x != y:  #如果两个位置的root不一样,
            self.root[x] = y  #把x位置的root放在x位置,也就是y是x的root.也就是用箭头把x,y连起来,x-->y,指向根.
            return True    #并且返回True
        else:      #如果root相同,说明已经连起来了,不用再做area加减法了.
            return False

    def inside(self, x, y, m, n):
        return x >= 0 and y >=0 and x < m and y < n

    def numIslands2(self, m, n, operators):
        # Write your code here
        d = [[0,1],[0,-1],[1,0],[-1,0]]
        area = 0
        ret = []
        for i in xrange(m * n):
            self.root.append(-1)
        for point in operators:
            num = point[0] * n + point[1]   #二维变一维后的下标
            if (self.root[num] == -1):         #如果这个下标上的数是-1,说明没遍历过,就是新添一个area
                area += 1
                self.root[num] = num           #把下标的数字存在这个位置

            for k in xrange(4):             #四个方向看一遍
                x = point[0] + d[k][0]     #x,y为四个方向在原matrix上的下标
                y = point[1] + d[k][1]

                if self.inside(x, y, m, n):  #如果没越界
                    if self.merge(x * n + y, num):  #这个num跟他的任一个方向能合并
                        area -= 1                   #area就-1.

            ret.append(area)

        return ret

if __name__ == '__main__':
    n = 3
    m = 3
    operators = [[0,0],[0,1],[1,1],[1,2],[2,2],[2,1]]
    s = Solution()
    print s.numIslands2(n,m,operators)