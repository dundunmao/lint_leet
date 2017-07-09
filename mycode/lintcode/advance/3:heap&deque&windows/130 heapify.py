# -*- encoding: utf-8 -*-
# 给出一个整数数组，堆化操作就是把它变成一个最小堆数组。

# 对于堆数组A，A[0]是堆的根，并对于每个A[i]，
# A[i * 2 + 1]是A[i]的左儿子,A[i * 2 + 2]是A[i]的右儿子。

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in range((len(A) - 1) / 2, -1, -1):
            self.siftdown(A, i)
        return A
    def siftdown(self, A, k):
        while k * 2 + 1 < len(A):
            son = k * 2 + 1
            if k * 2 + 2 < len(A) and A[son] > A[k * 2 + 2]:
                son = k * 2 + 2
            if A[son] >= A[k]:
                break
            A[son], A[k] = A[k], A[son]
            k = son