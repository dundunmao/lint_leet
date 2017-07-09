# coding:utf-8
# 3级
# 题目,在一个matrix里找target.这个matrix每行是sorted的,每行的头比它上一行的尾大
# 思路:binary search 先找到在哪一行,再在那行找那个数
def searchMatrix(matrix, target):
    if matrix is None or len(matrix) == 0:
        return False
    if matrix[0] is None or len(matrix[0]) == 0:
        return False
    if target < matrix[0][0]:
        return False
    x = float("inf")
    m = len(matrix)+1
    n = len(matrix[0])
    matrix.append([x]*n)
    for i in range(1, m):
        start = 0
        end = n-1
        if target < matrix[i][0] and target >= matrix[i-1][0]:
            target_line = i - 1
            while start + 1 < end:
                medium = start + (end - start) / 2
                if matrix[target_line][medium] > target:
                    end = medium
                if matrix[target_line][medium] < target:
                    start = medium
                if matrix[target_line][medium] == target:
                    return True
            if matrix[target_line][start] == target or matrix[target_line][end] == target:
                return True
            else:
                return False







if __name__ == '__main__':
    matrix = [[1,   3,  5,  7],
             [10, 11, 16, 20],
             [23, 30, 34, 50]]
    target = 3
    print searchMatrix(matrix, target)