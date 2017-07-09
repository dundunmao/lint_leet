# -*- encoding: utf-8 -*-
# 根据n皇后问题，现在返回n皇后不同的解决方案的数量而不是具体的放置布局。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如n=4，存在2种解决方案
class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens.
    @return: All distinct solutions.
    """

    def totalNQueens(self, n):
        # write your code here
        num = n
        cols = {}
        row = 0
        self.tot = 0
        self.search(row, num, cols)
        return self.tot

    def attack(self, row, col, cols):
        for c, r in cols.items():
            if c - r == col - row or c + r == col + row:
                return True
        return False

    def search(self, row, num, cols):
        if len(cols) == num:
            self.tot += 1
        for col in range(num):
            if col in cols:
                continue
            if self.attack(row, col, cols):
                continue
            cols[col] = row
            self.search(row + 1, num, cols)
            del cols[col]



class Solution1:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        result = []
        # record = []
        hash = {}
        row = 0
        self.helper(result,n,row,hash)

        return result

    def helper(self, result,n,row,hash):
        if len(hash) == n:
            line = []
            for i in range(n):
                r = ['.']*n
                r[hash[i]] = 'Q'
                line.append(''.join(r))
            result.append(line)
            return
        for col in range(0,n):
            # for col in range(0,n):
            if col in hash.values():
                continue
            elif self.attack(row,col,hash):
                continue
            else:
                hash[row] = col
                self.helper(result,n,row+1,hash)
                hash.pop(row)



    def attack(self, row, col, hash):
        for r,c in hash.items():
            if r-c == row-col or r+c == row+col:
                return True
        return False



if __name__ == '__main__':
    n=4
    s = Solution1()
    print s.solveNQueens(n)