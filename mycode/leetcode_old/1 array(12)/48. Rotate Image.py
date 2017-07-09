# -*- encoding: utf-8 -*-
# 2级
# 标签：Array
# 题目；把n*n的矩阵顺时针转90
# 思路：如果可以多开空间，先把他存在一个newMatrix里，然后 Matrix[i][j]=newMatrix[j][n-1-i]
#      如果不能新开，先纵向reverse，然后 matrix[i][j]=matrix[j][i]
#      或者 主意j的range分奇偶：matrix[i][j] = matrix[n-1-j][i]；
#                            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]；
#                            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]；
#                            matrix[j][n-1-i] = matrix[i][j]
#主要方法
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):  #这里是range(i),不是range(len(matrix[0]))
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def rotate2(matrix):
    n = len(matrix)
    if n%2:
        id = n//2 +1
    else:
        id = n//2
    for i in range(n//2):
        for j in range(id):
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[i][j]



if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print rotate(matrix)
    # print matrix
    # rotate(matrix)
    print matrix