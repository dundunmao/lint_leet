# -*- encoding: utf-8 -*-
# 给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。
#
#  注意事项
#
# 如果你只用额外空间复杂度O(n)的条件下完成可以获得加分，其中n是数字三角形的总行数。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如，给出下列数字三角形：
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。
#方法一,traverse的方法,但是Time Limit Exceeded
# 其time complex 是 O(2^n).因为每一个点都有2条路走,2*2*2*2....
class Solution1:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def __init__(self):
        self.mini = float('inf')   #不能作为参数往里传,只能作为全局变量存在
    def minimumTotal(self, triangle):
        self.helper(triangle,0,0,0)
        return self.mini
    #从(0,0)走到(x,y)
    def helper(self,triangle,x,y,sum):
        # when to return
        if x == len(triangle): #走过油了
            self.mini = min(self.mini,sum)
            return self.mini
        # traverse
        self.helper(triangle,x+1,y,sum+triangle[x][y])
        self.helper(triangle, x + 1, y+1, sum+triangle[x][y])
#第二种traverse
class Solution6(object):
    def __init__(self):
        self.res = float('inf')

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or triangle == []:
            return 0
        i = 0
        j = 0
        path = []
        self.helper(triangle, i, j, path)
        return self.res

    def helper(self, array, i, j, path):
        if i >= len(array):
            self.res = min(self.res, sum(path))
            return
        path.append(array[i][j])
        self.helper(array, i + 1, j, path)
        self.helper(array, i + 1, j + 1, path)
        path.pop()
# 方法二 Divid & conquer.还是超时
# 其time complex 是 O(2^n).
class Solution2:
    def minimumTotal(self, triangle):
        return self.helper(triangle,0,0)
    # 从(x,y)出发,走到最底层的mini
    def helper(self,triangle,x,y):
        # when to return
        if x == len(triangle): #走过油了
            return 0
        # traverse
        left = self.helper(triangle,x+1,y)
        right = self.helper(triangle, x + 1, y+1)
        return min(left,right)+ triangle[x][y]

# 方法二 Divid & conquer.优化,用hash
# 其time complex 是 O(n^2).
# 这个就是记忆化搜索的DP.
# 写搜索,然后加个hash就变成DP了
class Solution3:
    def minimumTotal(self, triangle):
        hash_record = {}   #起key为(x,y);value为triangle[x][y]
        return self.helper(triangle,0,0,hash_record)
    # 从(x,y)出发,走到最底层的mini
    def helper(self,triangle,x,y,hash_record):
        # when to return
        if x == len(triangle): #走过油了
            return 0
        if hash_record.has_key((x,y)):
            return hash_record[(x,y)]
        # traverse
        left = self.helper(triangle,x+1,y,hash_record)
        right = self.helper(triangle, x + 1, y+1,hash_record)
        hash_record[(x,y)] = min(left,right)+ triangle[x][y]
        return hash_record[(x,y)]

# DP
# 去掉重复运算.算过的存起来
# 二叉树没有重复运算,所以用分治没问题.
# 三角型,棋盘的,有重复走的点,用分治会超时.要用DP去算.

# DP Bottom-Up
class Solution4:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        if triangle is None or len(triangle) == 0:
            return -1
        if triangle[0] is None or len(triangle[0]) == 0:
            return -1

        # state: f[x][y] = minimum path value from x,y to bottom
        n = len(triangle)
        f =  [[0 for col in range(n)] for row in range(n)]
        # initialize
        for i in range(0,n):
            f[n - 1][i] = triangle[n - 1][i]
        # bottom up
        for i in range(n-2, -1, -1):
            for j in range(0,i+1):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]

        return f[0][0]
# DP: top-down
class Solution5:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        if triangle is None or len(triangle) == 0:
            return -1
        if triangle[0] is None or len(triangle[0]) == 0:
            return -1

        # state: f[x][y] = minimum path value from 0,0 to x,y
        n = len(triangle)
        # 初始化矩阵
        f =  [[0 for col in range(n)] for row in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1,n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        # // top down
        for i in range(1,n):
            for j in range(1,i):
                f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
        # // 最后一行所以node取最小
        best = mini = min(f[n - 1][i] for i in range(0, n))
        return best




if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
    ]

    # [6, 5, 7],
    # [4, 1, 8, 3]
    s = Solution6()
    print s.minimumTotal(triangle)