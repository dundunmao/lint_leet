# -*- encoding: utf-8 -*-
# n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击。
#
# 给定一个整数n，返回所有不同的n皇后问题的解决方案。
#
# 每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 对于4皇后问题存在两种解决的方案：
#
# [
#
#     [".Q..", // Solution 1
#
#      "...Q",
#
#      "Q...",
#
#      "..Q."],
#
#     ["..Q.", // Solution 2
#
#      "Q...",
#
#      "...Q",
#
#      ".Q.."]
#
# ]
class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens.
    @return: All distinct solutions.
    """

    def solveNQueens(self, n):
        # write your code here
        num = n
        results = []
        cols = {}
        row = 0
        self.search(row, num, results, cols)
        return results

    def attack(self, row, col, cols):
        for c, r in cols.items():
            if c - r == col - row or c + r == col + row:
                return True
        return False

    def search(self, row, num, results, cols):
        # if row == num:#定好一个col,row就开始从0遍历,没走一个row,col从0遍历,一旦col遍历到头,就证明尝试失败.
        if len(cols) == num:
            result = []

            for i in range(num):
                r = ['.'] * num
                r[cols[i]] = 'Q'
                result.append(''.join(r))
            results.append(result)
            return

        for col in range(num):
            if col in cols:
                continue
            if self.attack(row, col, cols):
                continue
            cols[col] = row
            self.search(row + 1, num, results, cols)
            del cols[col]


if __name__ == '__main__':
    n=4
    s = Solution()
    print s.solveNQueens(n)