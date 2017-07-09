# coding:utf-8
# 给定一个N×N的二维矩阵表示图像，90度顺时针旋转图像。
#
#
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出一个矩形[[1,2],[3,4]]，90度顺时针旋转后，返回[[3,1],[4,2]]
class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        if n == 1 or n == 0:
            return matrix
        for array in matrix:
            array.reverse()
        for i in range(0,n):
            for j in range(0,n-i):
                matrix[i][j], matrix[(n-1)-j][(n-1)-i] = matrix[(n-1)-j][(n-1)-i],matrix[i][j]
        return matrix
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):  #这里是range(i),不是range(len(matrix[0]))
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

class Solution_leet(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0:
            return
        if matrix[0] is None or len(matrix[0]) <= 1:
            return
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix



if __name__ == "__main__":
    s = Solution_leet()
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix = [[1,2],[3,4]]
    print s.rotate(matrix)
    # print matrix
    # rotate(matrix)
    # print matrix