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


#create一个index，给所有数从左到右从上到下编号，每个数在两个matrix里的编号就是一样的。然后
# 在原matrix里，index = i*len_col+j
# 在新matrix里，i = index // c
#             j = index % c
class Solution2(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        le_row = len(nums)
        le_col = len(nums[0])
        if le_row * le_col != r * c:
            return nums

        result = [[None for j in range(c)] for i in range(r)]
        for i in range(le_row):
            for j in range(le_col):
                index = i * le_col + j
                # nums[i][j] = [index,nums[i][j]]
                row = index // c
                col = index % c
                result[row][col] = nums[i][j]
        return result
if __name__ == "__main__":
    nums = [[1,2],[3,4]]
    r= 1
    c = 4
    x = Solution2()
    print x.matrixReshape(nums, r, c)