# -*- encoding: utf-8 -*-
# 同类题
# easy 268. Missing Number
# easy 645. Set Mismatch
# easy 448. Find All Numbers Disappeared in an Array
# med 442. Find All Duplicates in an Array
# med 287. Find the Duplicate Number
# hard  41. First Missing Positive
# 让1就在第一位，2就在第二位，每个数都在第几位
# A[A[i] - 1] != A[i] 以ele为index的位置上的元素是不是这个ele

class Solution(object):
    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(A):
            if A[i] == i+1 or A[i] <= 0 or A[i] > len(A):
                i+=1
            elif A[A[i]-1] != A[i]:
                self.swap(A,i,A[i]-1)
            else:
                i+=1
        i = 0
        while i < len(A) and A[i] == i+1:
            i += 1
        return i+1
    def swap(self,A,i,j):
        A[i],A[j] = A[j],A[i]
        return A


class Solution1(object):
    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if A == []:
            return 1
        for i in range(len(A)):
            # A[i] > 0 要先判断（A[i]小于0就不用管它了），
            # 然后判断A[i] - 1 < len(A)（A[i]这个index超没超界）
            # 这里是A[A[i] - 1] != A[i]而不是A[i] - 1 != i（以ele为index的位置上的元素是不是这个ele，为解决【1，1】这种情况）
            while A[i] > 0 and A[i] - 1 < len(A) and A[A[i] - 1] != A[i]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

        for i, ele in enumerate(A):
            if ele - 1 != i:
                return i + 1

        return len(A) + 1  #这句是为了解决【1，2，3】这种情况，return 4

if __name__ == "__main__":
    a = [2]
    x = Solution1()
    print x.firstMissingPositive(a)