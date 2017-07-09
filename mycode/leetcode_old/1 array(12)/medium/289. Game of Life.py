# coding:utf-8
# 给出一个m*n的细胞矩阵，每个细胞都有一个初始状态：生存（1）或死亡（0）。每个细胞的变化都与它周围8个细胞有关，规则如下：
# 当前细胞为存活状态时，当周围存活细胞不到2个时， 该细胞变成死亡状态。（模拟生命数量稀少）
# 当前细胞为存活状态时，当周围有2个或3个存活的细胞时， 该细胞保持原样。#
# 当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
# 当前细胞为死亡状态时，当周围恰好有3个存活细胞时，该细胞变成存活状态。 （模拟繁殖）
# 写一个函数，根据矩阵当前的状态，计算这个细胞矩阵的下一个状态。要求in-place
#0,2 are "dead", and "dead->live" 1,3 are "live", and "live->dead"
def gameOfLife(board):
    m,n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0 or board[i][j] == 2: #如果是0(dead)
                if nnb(board,i,j) == 3:              #周围加起来是3
                    board[i][j] = 2                  #那他就是2(dead->live)
            else:                                    #如果是live
                if nnb(board,i,j) < 2 or nnb(board,i,j) >3:# 周围加起来小于2或大于3
                    board[i][j] = 3                        #那他就是3(live->dead)
    for i in range(m):          #重新更新表格,让2"dead->live"变为1(live),3"live->dead"变为0(dead)
        for j in range(n):
            if board[i][j] == 2: board[i][j] = 1
            if board[i][j] == 3: board[i][j] = 0

def nnb(board, i, j):
    m,n = len(board), len(board[0])
    count = 0
    #一共8个if,要把他邻居的八个数都算进去
    if i-1 >= 0 and j-1 >= 0:     #如果不是第一排,也不是第一列 (说明他最上角一定有格子)
        count += board[i-1][j-1]%2      #左上角的格子列入count中
    if i-1 >= 0:                  #如果不是第一排的数()
        count += board[i-1][j]%2        #其上方的格子列入count中
    if i-1 >= 0 and j+1 < n:      #如果不是第一排,也不是最后一列()
        count += board[i-1][j+1]%2      #右上角的格子列入count中
    if j-1 >= 0:                   #如果不是第一列()
        count += board[i][j-1]%2        #前方的格子列入count中
    if j+1 < n:                    #如果不是最后一列()
        count += board[i][j+1]%2        #后方的格子列入count中
    if i+1 < m and j-1 >= 0:       #如果不是最后一排,也不是第一列()
        count += board[i+1][j-1]%2      #左下角的格子列入count中
    if i+1 < m:                     #如果不是最后一排()
        count += board[i+1][j]%2        #下方的格子列入count中
    if i+1 < m and j+1 < n:         #如果不是最后一排,也不是最后一列(说明右下角一定有格子)
        count += board[i+1][j+1]%2      #右下角角的格子列入count中
    return count




if __name__ == '__main__':
    board = [[0,0,0,0,0],
             [0,0,1,0,0],
             [0,0,1,0,0],
             [0,0,1,0,0],
             [0,0,0,0,0]]
    print gameOfLife(board)