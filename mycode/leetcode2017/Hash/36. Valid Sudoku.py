# -*- encoding: utf-8 -*-

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #  对于每一行
        for i in range(9):
            row = {}
            for j in range(9):
                if board[i][j] != '.' and row.has_key(board[i][j]):
                    return False
                else:
                    row[board[i][j]]=True
        #  对于每一列
        for j in range(9):
            col = {}
            for i in range(9):
                if board[i][j] != '.' and col.has_key(board[i][j]):
                    return False
                else:
                    col[board[i][j]] = True
        #  对于每一个cube
        for i in range(9):
            cube = {}
            for j in range(9):
                row_index = 3*(i/3)
                col_index = 3*(i%3)
                if board[row_index+j/3][col_index + j%3] != '.' and cube.has_key(board[row_index + j/3][col_index + j%3]):
                    return False
                else:
                     cube[board[row_index + j/3][col_index + j%3]] = True
        return True