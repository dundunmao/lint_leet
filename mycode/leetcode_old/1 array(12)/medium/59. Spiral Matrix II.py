# coding:utf-8
# 3级
# 题目:给一个n.要把1到n平方的数spiral顺序填入到matrix里.返回matrix

# def generateMatrix(n):
#     matrix = [[0]*n for i in range(n)]
#     for i in n:

def generateMatrix(n):
    A = [[0] * n for _ in range(n)]    #如何建立一个matrix
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n*n):
        A[i][j] = k + 1                 #第一个数从1开始
        if A[(i+di)%n][(j+dj)%n]:       #如果A[(i+di)%n][(j+dj)%n]不为0,就是如果到头了(前方不是0了),就右转
            di, dj = dj, -di            #右转
        i += di                         #di初始值是0,所以相当于保持在这一行不动
        j += dj                         #dj初始值是1,所以相当于往右遍历
    return A
if __name__ == '__main__':
    n = 4
    print generateMatrix(n)
