# coding:utf-8
# 3.5级
# 题目:给定一个二维字母数组和一个word.问这个Word是否在这个数组里.横竖相连的字母才能组成数字例如
# Given board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
        """
    if not word:
        return True
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if exist_helper(board, word, i, j):
                return True
    return False

def exist_helper(board, word, i, j):
    if board[i][j] == word[0]:  #如果遍历到的这个数是Word的第一个字母,就往下检查,否则return false
        if not word[1:]:        #如果Word只有一个字母,return True
            return True
        board[i][j] = " "   # indicate used cell,因为同一个字母不能用两次
        # check all adjacent cells
        if i > 0 and exist_helper(board, word[1:], i-1, j):             #往上遍历
            return True
        if i < len(board)-1 and exist_helper(board, word[1:], i+1, j):  #往下遍历
            return True
        if j > 0 and exist_helper(board, word[1:], i, j-1):             #往左遍历
            return True
        if j < len(board[0])-1 and exist_helper(board, word[1:], i, j+1):   #往右遍历
            return True
        # board[i][j] = word[0] # update the cell to its original value
        return False
    else:
        return False  #跳出什么了???????


if __name__ == '__main__':
    board=[
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word = "ABCCED"
    print exist(board, word)