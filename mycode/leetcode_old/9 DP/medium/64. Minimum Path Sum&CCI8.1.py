# coding:utf-8
# 题目:r*c的方格子,robot只能超右和超下走.请找出一个path
# 思路:f(m,n) =min(f(m,n-1),f(m-1,n))+grid[m][n]

# dynamic programming
# 第一行是前面的数加自己,第一列是上面的数加自己.剩下的格子为上面的和前面的取最大再加自己

def minPathSum(self, grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


#用recursive 做的,虽然对,但是时间太长了
def minpath(grid):
    m = len(grid)
    n = len(grid[0])
    # 边界条件:当只有一个数,只有一行,只有一列的时候
    if m == 1 and n == 1:
        return grid[m-1][n-1]
    if m ==1:
        return sum(grid[0])
    if n == 1:
        sum1 = 0
        for i in range(m):
            sum1+=grid[i][0]
        return sum1
    #少一行的矩阵表示
    new_grid_1 = grid[1:]
    #少一列的矩阵表示
    new_grid_2 = []
    for i in range(m):
        new_grid_2.append(grid[i][1:])
    #状态方程
    return grid[0][0]+min(minpath(new_grid_1),minpath(new_grid_2))

if __name__ == '__main__':
    grid = [[3,4,4,5,7,7],
            [3,2,1,4,5,6],
            [4,5,4,3,6,7]]

    print minpath(grid)

    grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]

    print minpath(grid)
# if __name__ == '__main__':
#     # #case1: illegel case:
#     # grid  = [1,2,3]
#     # print mini_path(grid)
#     #
#     # #case2: edge case:
#     # grid = []
#     # print mini_path(grid)
#
#     # case 3: normal input 1:
#     grid = [[1,2],[2,3]]
#     print mini_path(grid)
#
#     # case 4: normal input 2