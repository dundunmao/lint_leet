# -*- encoding: utf-8 -*-
# 2级
# 内容：在list里 nums[i]等于所以element除nums[i]之外的和.例如given [1,2,3,4], return [24,12,8,6]
# 思路: 一个循环求每个数之前所有数之积,另一个循环求每个数之后所有数之积,然后相乘

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        forward = 1
        #scan forward
        for i in xrange(1,len(nums)):
            forward=forward*nums[i-1]
            res.append(forward)
        #scan backward
        backward = 1
        for i in xrange(len(nums)-2,-1,-1):
            backward = backward*nums[i+1]
            res[i]=res[i]*backward


        return res
if __name__ =="__main__":
    nums = [1,2,3,4]
    # nums = [1,1,2,4,4,5,5,5,7]
    # val = 5
    s = Solution()
    print s.productExceptSelf(nums)