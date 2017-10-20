# -*- encoding: utf-8 -*-
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0:
            return
        self.helper(board)
    def helper(self,board):
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == '.':   #找到空位
                    for num in range(1,10):  #把十个数分别往里面放，看valid不。
                        num = str(num)
                        if self.isValid(board,i,j,num):  # 如果找到valid的
                            board[i][j] = num            # 1：把这个valid的数字填上
                            if self.helper(board):       # 检查整体为True
                                return True              # 就返回True
                            else:
                                board[i][j] = '.'        # 否则填上 '。'
                    return False                        #所以都尝试过都不好使，返回False
        return True
    def isValid(self,board,row,col,num):
        for i in range(0,9):
            if board[i][col] != '.' and board[i][col] == num:  #如果这一行有这个数字，就False
                return False
            if board[row][i] != '.' and board[row][i] == num:  #如果这一列有这个数字，就False
                return False
            if board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] != '.' and board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == num:
                return False                                   #如果这一cube有这个数字，就False
        return True