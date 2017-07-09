# -*- encoding: utf-8 -*-
# 题目: 在数组中找到第k大的元素
# heap 方法
import heapq
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, A,k):
        if A is None or len(A)==0:
            return 0
        q = []
        for i in range(len(A)):
            A[i] = -A[i]
        heapq.heapify(A)
        node = 0
        for i in range(k):
            node = heapq.heappop(A)
        return -node
# 双指针法
class Solution1:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, A,k):
        if A is None or len(A) == 0:
            return 0
        if k <= 0:
            return 0
        return self.helper(A, 0, len(A) - 1, len(A) - k + 1)

    def helper(self, nums, l, r, k):
        if l == r:
            return A[l]
        position = self.partition(A, l, r)
        if position + 1 == k:
            return A[position]
        elif position + 1 < k:
            return self.helper(A, position + 1, r, k)
        else:
            return self.helper(A, l, position - 1, k)

    def partition(self, A, l, r):
        pivot = A[l]
        while l < r:
            while l < r and A[r] >= pivot:
                r -= 1
            A[l] = A[r]
            while l < r and A[l] <= pivot:
                l += 1
            A[r] = A[l]
        A[l] = pivot
        return l
if __name__ == "__main__":
    A = [1,2,3,4,5,6,8,9,10,7] # ans = 3
    A = [9,3,2,4,8]  # ans = 4

    k = 10
    k = 4
    s = Solution1()

    print s.kthLargestElement(A, k)