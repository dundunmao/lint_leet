# coding:utf-8

# 写出一个高效的算法来搜索 m × n矩阵中的值。
#
# 这个矩阵具有以下特性：
#
# 每行中的整数从左到右是排序的。
# 每行的第一个数大于上一行的最后一个整数。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 考虑下列矩阵：
#
# [
#   [1, 3, 5, 7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# 给出 target = 3，返回 true
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
# O(n^2)
    def searchMatrix(self, matrix, target):
        # write your code here
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

# O(log(n) + log(m))
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False
        if target < matrix[0][0]:
            return False
        start_row = 0
        end_row = len(matrix)-1
        while start_row+1 < end_row:
            mid_row = start_row + (end_row - start_row) / 2
            if matrix[mid_row][0] < target:
                start_row = mid_row
            elif matrix[mid_row][0] > target:
                end_row = mid_row
            else:
                return True
        if target < matrix[start_row][0]:
            row = start_row - 1
        elif target < matrix[end_row][0]:
            row = start_row
        else:
            row = end_row
        start = 0
        end = len(matrix[0])-1
        while start + 1 < end:
            mid = start + (end - start)/2
            if matrix[row][mid] < target:
                start = mid
            elif matrix[row][mid] > target:
                end = mid
            else:
                return True
        if target == matrix[row][start] or target == matrix[row][end]:
            return True
        else:
            return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # edge case
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False
        # excute
        m = len(matrix)
        n = len(matrix[0])
        s = 0
        e = m * n - 1
        while s + 1 < e:
            mid = (s + e) / 2
            row = mid / n
            col = mid % n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                e = mid
            else:
                s = mid
        s_row = s / n
        s_col = s % n
        e_row = e / n
        e_col = e % n
        if target == matrix[s_row][s_col] or target == matrix[e_row][e_col]:
            return True
        else:
            return False

if __name__ == "__main__":
    A = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 3
    s = Solution()
    print s.searchMatrix2(A,target)