# coding:utf-8
# 给你一个二维矩阵，权值为False和True，找到一个最大的矩形，使得里面的值全部为True，输出它的面积
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给你一个矩阵如下
#
# [
#   [1, 1, 0, 0, 1],
#   [0, 1, 0, 0, 1],
#   [0, 0, 1, 1, 1],
#   [0, 0, 1, 1, 1],
#   [0, 0, 0, 0, 1]
# ]
# 输出6
class Solution:
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    def maximalRectangle(self, matrix):
        # Write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        result = float('-inf')
        r_array = [0]*len(matrix[0])
        r_array.append(-1)
        for k in range(len(matrix)):
            # if matrix[i] == 1:
            #     result = max(result, matrix[i])
            for j in range(len(matrix[0])):
                if matrix[k][j] == 0:
                    r_array[j] = 0
                else:
                    r_array[j] = r_array[j] + matrix[k][j]
            result = max(result, self.histogram(r_array))
        return result

    def histogram(self, hei):
        maxi = float('-inf')
        stack = []
        # hei.append(-1)
        for i in range(len(hei)):

            while len(stack) != 0 and hei[i] < hei[stack[-1]]:
                h = hei[stack.pop()]
                if len(stack) == 0:
                    w = i
                else:
                    w = i-stack[-1]-1
                maxi = max(maxi,h*w)
            stack.append(i)
        return maxi
#f方法二，robin的方法
class Solution_leet(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0:
            return 0
        matrix = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]

        row = len(matrix)
        ans = 0
        for i in range(row - 1, -1, -1):
            col = []
            for k in range(0, len(matrix[0])):
                ele = 0
                for j in range(i, -1, -1):
                    if matrix[j][k] == 1:
                        ele += 1
                    else:
                        break
                col.append(ele)
            ans = max(ans, self.histogram(col))
        return ans

    def histogram(self, A):
        # return maximum rectanglu
        l = [0 for i in range(len(A))]
        r = [0 for j in range(len(A))]
        res = 0
        for i in range(len(A)):
            l[i] = i
            while l[i] > 0 and A[i] <= A[l[i] - 1]:
                l[i] = l[l[i] - 1]
        for i in range(len(A) - 1, -1, -1):
            r[i] = i
            while r[i] < len(A) - 1 and A[i] <= A[r[i] + 1]:
                r[i] = r[r[i] + 1]
        for i in range(len(A)):
            res = max(res, A[i] * (r[i] - l[i] + 1))
        return res
if __name__ == "__main__":

    m = [
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1]
    ]
    # m = [[1,0,1,0,0], [1,0,1,1,1], [1,1,1,1,1], [1,0,0,1,0]]
    s = Solution1()
    print s.maximalRectangle(m)