# -*- encoding: utf-8 -*-
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        if row * col != r * c:
            return nums
        A = []

        for i in range(row):
            A.extend(nums[i])
        k = 0
        result = [[None for j in range(c)] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if k >= len(A):
                    break
                result[i][j] = A[k]
                k += 1
        return result
if __name__ == "__main__":
    nums = [[1,2],[3,4]]
    r= 1
    c = 4
    x = Solution()
    print x.matrixReshape(nums, r, c)