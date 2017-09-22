# -*- encoding: utf-8 -*-
# 写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。
#
# 这个矩阵具有以下特性：
#
# 每行中的整数从左到右是排序的。
# 每一列的整数从上到下是排序的。
# 在每一行或每一列中没有重复的整数。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 考虑下列矩阵：
#
# [
#
#     [1, 3, 5, 7],
#
#     [2, 4, 7, 8],
#
#     [3, 5, 9, 10]
#
# ]
#
# 给出target = 3，返回 2
class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    # O(m * n)
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return 0
        if matrix[0] is None or len(matrix[0]) == 0:
            return 0
        if target < matrix[0][0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        for i in range(m):
            start = 0
            end = n-1
            while start + 1 < end:
                medium = start + (end - start) / 2
                if target < matrix[i][medium]:
                    end = medium
                elif target > matrix[i][medium]:
                    start = medium
                elif target == matrix[i][medium]:
                    count += 1
                    break   #while里的用break因为一行就一个找到就可以找下一行了
            if target == matrix[i][start]:
                count += 1
                continue    # for里的用continue
            elif target == matrix[i][end]:
                count += 1
                continue
        return count

    # O(m+n)
    def searchMatrix1(self, matrix, target):
        if matrix is None or len(matrix) == 0:
            return 0
        if matrix[0] is None or len(matrix[0]) == 0:
            return 0
        if target < matrix[0][0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        x = n - 1
        y = 0
        while x >=0 and y<m:
            if matrix[x][y] < target:
                y+=1
            elif matrix[x][y] > target:
                x -=1
            else:
                count += 1
                x -= 1
                y += 1
        return count

    def searchMatrix_leetcode(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        row = m-1
        col = 0
        while row >= 0 and col <= n - 1:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False
if __name__ == "__main__":
    A = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    s = Solution()
    print s.searchMatrix(A,target)