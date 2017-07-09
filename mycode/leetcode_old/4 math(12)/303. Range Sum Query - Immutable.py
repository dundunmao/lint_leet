# -*- encoding: utf-8 -*-
# 标签：math，dp
# 题目；给一个list,算第i到第j之间的数的和
# 思路：(0-j)的和减去（0-i）的和
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if nums == []:
           return
        self.accu = [nums[0]]
        for k in range(1,len(nums)):
            self.accu.append( self.accu[k-1] + nums[k])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.accu[j]
        else:
            return self.accu[j] - self.accu[i-1]


if __name__ == "__main__":
    nums = [-2,0,3,-5,2,-1]
    numArray = NumArray(nums)
    print numArray.sumRange(0, 2)
    print numArray.sumRange(2, 5)
    print numArray.sumRange(0, 5)