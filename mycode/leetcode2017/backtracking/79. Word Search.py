# -*- encoding: utf-8 -*-
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.'


# DFS
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
    def exist(self, board, word):
        # write your code here
        # Boundary Condition
        if word == []:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        # Visited Matrix
        visited = [[False for j in range(n)] for i in range(m)]
        # DFS
        for i in range(m):
            for j in range(n):
                if self.helper(board, word, visited, i, j): #找matrix上每个位置能不能word_search,
                    return True                             #找到一个就return
        return False

    def helper(self, board, word, visited, row, col):     #从(row,col)这个位置起，找word = 看四个方向能找到word[1:]不
        if word == '':      #出口，空word返回True
            return True
        m, n = len(board), len(board[0])
        if row < 0 or row >= m or col < 0 or col >= n:  #如果row，col越界，就false
            return False
        if board[row][col] == word[0] and not visited[row][col]:  #如果当前位置正好(row,col)是word的第一个char，
            visited[row][col] = True                                # 1，visit标记
                                                                    # 2，四个方向有一个方向是True,就return True
            if self.helper(board, word[1:], visited, row - 1, col) \
            or self.helper(board, word[1:], visited, row, col - 1) \
            or self.helper(board, word[1:], visited, row + 1, col) \
            or self.helper(board, word[1:], visited, row, col + 1):
                return True
            else:  #如果四个方向都false，把这个之前标记的visit去掉
                visited[row][col] = False
        return False



from collections import deque
import copy
# 这里我用了bfs，但是要记得每一个路线都要有自己的hash，我只是initail的时候有几个起点，就创建了几个hash，但如果后面分叉多，hash并不会增加
# 所以这里每次往q里添加新的node时，hash都是用的硬拷贝。
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        cor = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(board)
        n = len(board[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    q.append([(i, j), 0, {(i, j): True}])
        if len(word) == 1:
            return len(q) != 0
        while q:
            size = len(q)
            for k in range(size):
                cur, pos, hash_cur = q.popleft()
                if pos == len(word) - 1:
                    return False
                for i, j in cor:
                    if cur[0] + i > -1 and cur[0] + i < m and cur[1] + j > -1 and cur[1] + j < n and pos + 1 == len(
                            word) - 1 and (cur[0] + i, cur[1] + j) not in hash_cur and board[cur[0] + i][cur[1] + j] == \
                            word[pos + 1]:
                        return True
                    if cur[0] + i > -1 and cur[0] + i < m and cur[1] + j > -1 and cur[1] + j < n and (
                        cur[0] + i, cur[1] + j) not in hash_cur and board[cur[0] + i][cur[1] + j] == word[pos + 1]:
                        hash_i = copy.deepcopy(hash_cur)
                        hash_i[(cur[0] + i, cur[1] + j)] = True
                        q.append([(cur[0] + i, cur[1] + j), pos + 1, hash_i ])
        return False






if __name__ == '__main__':
    s = Solution()
    a = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    b = "ABCESEEEFS"
    print s.exist(a,b)
