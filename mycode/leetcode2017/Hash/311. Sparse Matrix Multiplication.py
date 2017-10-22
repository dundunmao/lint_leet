# -*- encoding: utf-8 -*-
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            return False
        C = [[0 for j in range(l)] for i in range(m)]
        table_A, table_B = {}, {}  #key为行序号i，value里面存第i行的那个array（但此array存为key为index，value为值的hash里）
        for i, row in enumerate(A):
            for j, ele in enumerate(row):
                if ele:
                    if i not in table_A: table_A[i] = {}
                    table_A[i][j] = ele
        for i, row in enumerate(B):
            for j, ele in enumerate(row):
                if ele:
                    if i not in table_B: table_B[i] = {}
                    table_B[i][j] = ele
        for i in table_A:
            for k in table_A[i]:
                if k not in table_B:
                    continue
                for j in table_B[k]:
                    C[i][j] += table_A[i][k] * table_B[k][j]
        return C

# 超时
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            return False
        C = [[0 for j in range(l)] for i in range(m)]
        table_A, table_B = {}, {}  #key为行序号i，value里面存第i行的那个array（但此array存为key为index，value为值的hash里）
        for i, row in enumerate(A):
            for j, ele in enumerate(row):
                if ele:
                    if i not in table_A: table_A[i] = {}
                    table_A[i][j] = ele
        for i, row in enumerate(B):
            for j, ele in enumerate(row):
                if ele:
                    if i not in table_B: table_B[i] = {}
                    table_B[i][j] = ele
        for i in range(m):
            for j in range(l):
                for k in range(n):
                    if A[i][k] != 0 and B[k][j] != 0:
                            C[i][j] += A[i][k] * B[k][j]
        return C