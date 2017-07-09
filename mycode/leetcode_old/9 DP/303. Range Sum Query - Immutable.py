# -*- encoding: utf-8 -*-
# 题目:Given an integer array nums, 得到indices i and j(inclusive)直接的sum.
# 例如:Given nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
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



# Your NumArray object will be instantiated and called as such:
if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print numArray.sumRange(0, 1)
    print numArray.sumRange(1, 2)



class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.updatedlist = []
        self.updateList()

    def updateList(self):
        if len(self.nums) >0:
            self.updatedlist.append(self.nums[0])
        for i in range(1,len(self.nums)):
            self.updatedlist.append(self.updatedlist[i-1] + self.nums[i])



    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = self.updatedlist[j]
        if i >=1:
            sum -= self.updatedlist[i-1]
        return sum

#_____________________________________________
#我的方法

def sum_from_start(nums,k):
    result = 0
    for m in range(0,k+1):
        result += nums[m]
    return result

def sumR(i,j):
    if i == 0:
        return sum_from_start(nums,j)
    else:
        return sum_from_start(nums,j)-sum_from_start(nums,i-1)



if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    print sumR(0, 2)
    print sumR(2, 5)
    print sumR(0, 5)