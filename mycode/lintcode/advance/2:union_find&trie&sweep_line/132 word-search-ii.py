# -*- encoding: utf-8 -*-
class TrieNode:
    def __init__(self):
        self.flag = False
        self.s = ''
        self.sons = []
        for i in range(26):
            self.sons.append(None)


class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        # Write your code here
        cur = self.root
        for i in range(len(word)):
            c = ord(word[i]) - ord('a')
            if cur.sons[c] is None:
                cur.sons[c] = TrieNode()
            cur = cur.sons[c]
        cur.s = word
        cur.flag = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        # Write your code here
        cur = self.root
        for i in range(len(word)):
            c = ord(word[i]) - ord('a')
            if cur.sons[c] is None:
                return False
            cur = cur.sons[c]
        return cur.flag

class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        result = []
        tree = Trie()
        for word in words:
            tree.insert(word)
        res = ''
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.help(board,i,j,tree.root,result,res)
        return result
    def help(self,board,x,y,root,result,res):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        if root.flag is True:
            if root.s not in result:
                result.append(root.s)
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y]==0 or root is None:
            return
        if root.sons[ord(board[x][y]) - ord('a')]:
            for i in range(4):
                cur = board[x][y]
                board[x][y] = False
                self.help(board, x+dx[i], y+dy[i],root.sons[ord(cur) - ord('a')], result, res)
                board[x][y] = cur
if __name__ == '__main__':
    board = [
        ['d','o','a','f'],
        ['a','g','a','i'],
        ['d','c','a','n']
    ]
    words =["dog", "dad", "dgdg", "can", "again"]


    s = Solution()
    print s.wordSearchII(board, words)