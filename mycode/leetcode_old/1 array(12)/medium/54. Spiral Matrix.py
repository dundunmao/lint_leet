# coding:utf-8
# 3级
# 题目:Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.给定一个matrix,使其以漩涡order输出
# #例如
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        while matrix:
            ret += matrix.pop(0)                # 1.先把第一排存进去.并且这一排pop出去了.
            if matrix and matrix[0]:            # 2.对于新的matrix(除去第一排的),分别把每一排的最后一个数存进去,并且也pop出去
                for row in matrix:
                    ret.append(row.pop())
            if matrix:                          # 3.对于新的matrix(除去第一排和最后一列的),pop出最后一个element(就是最后一排)然后用[::-1]给倒过来
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:            # 4.对于新的matrix(除去第一排,最后一列,最后一排)倒着把每一排的第一个数pop出来.
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret

if __name__ == '__main__':
    matrix = [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
    s = Solution()
    print(s.spiralOrder(matrix))