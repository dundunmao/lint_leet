# -*- encoding: utf-8 -*-
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# 给一个n*m的矩阵，里面只有0-dead,1-live。存在的条件如上：每个点，其四周有8个邻居
# 1：此点为1，邻居少于两个1，这个点为0
# 2：此点为1，邻居为为两个1或三个1，这个点为1
# 3：此点为1，邻居为多余三个1，这个点为0
# 4：此点为0，邻居为三个1，这个点为1

#
# in-place的做法，先检查当前位置是否变化，如果变化了
# 原来是1，就让他变成-1，
# 原来是0，就让他变成-2
# 这样就不会影响原来计算，再循环一次再改回来，把-1改成0，把-2改成1
class Solution1(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or board == [[]]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                x = self.if_change(board, i, j) #这里跟下面的方法不一样，这里返回的是是否改变状态了。
                if x == False:
                    continue
                else:
                    if board[i][j] == 1:
                        board[i][j] = -1
                    elif board[i][j] == 0:
                        board[i][j] = -2
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == -2:
                    board[i][j] = 1
        print board
    def if_change(self, board, i, j):
        num = self.nerighor(board, i, j)
        if board[i][j] == 1:
            if num < 2:
                return True
            elif num == 2 or num == 3:
                return False
            elif num > 3:
                return True
        elif board[i][j] == 0 and num == 3:
            return True

        return False

    def nerighor(self, board, i, j):  # how many 1
        x = [1, -1, 0]
        y = [1, -1, 0]
        m = len(board)
        n = len(board[0])
        sum = 0
        for x1 in x:
            for y1 in y:
                if x1 == 0 and y1 == 0:
                    continue
                if i + x1 >= 0 and i + x1 < m and j + y1 >= 0 and j + y1 < n and abs(board[i + x1][j + y1]) == 1:
                    sum += 1
        return sum

# 新开一块空间存结果,该改成什么，就是什么
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or board == [[]]:
            return board
        m = len(board)
        n = len(board[0])
        result = [[None for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                x = self.change(board, i, j)
                if x == None:
                    result[i][j] = board[i][j]
                else:
                    result[i][j] = x
        return result

    def change(self, board, i, j): #返回[i,j]这个位置应该改成什么
        num = self.nerighor(board, i, j)
        if board[i][j] == 1:
            if num < 2:
                return 0
            elif num == 2 or num == 3:
                return 1
            elif num > 3:
                return 0
        elif board[i][j] == 0 and num == 3:
            return 1

        return None

    def nerighor(self, board, i, j):  # how many 1
        x = [1, -1, 0]
        y = [1, -1, 0]
        m = len(board)
        n = len(board[0])
        sum = 0
        for x1 in x:
            for y1 in y:
                if x1 == 0 and y1 == 0:
                    continue
                if i + x1 >= 0 and i + x1 < m and j + y1 >= 0 and j + y1 < n and board[i + x1][j + y1] == 1:
                    sum += 1
        return sum
if __name__ == "__main__":
    a = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    x = Solution1()
    print x.gameOfLife(a)
    # print x.nerighor(a,2,0)
    # print x.status(a,2,3)