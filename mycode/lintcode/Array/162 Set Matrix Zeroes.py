# coding:utf-8
# 给定一个m×n矩阵，如果一个元素是0，则将其所在行和列全部元素变成0。
#
# 需要在原矩阵上完成操作。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一个矩阵
#
# [
#   [1, 2],
#   [0, 3]
# ]
# 返回
#
# [
#   [0, 2],
#   [0, 0]
# ]

class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        array_x = []
        array_y = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    array_x.append(i)
                    array_y.append(j)
        for i in array_x:
            matrix[i] = [0]*n
        for i in range(m):
            for j in array_y:
                matrix[i][j] = 0
        return matrix
if __name__ == "__main__":
    s = Solution()
    m = [
            [1, 2],
            [0, 3]
        ]

    print s.setZeroes(m)



