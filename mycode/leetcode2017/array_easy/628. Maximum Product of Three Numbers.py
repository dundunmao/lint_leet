# -*- encoding: utf-8 -*-
# 找数组里三个数的乘积最大
# 解题：排序后，要么就是最后三个的乘积，要么就考虑有负数，前两个是最小的负数，再乘最后一个数
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a,b)

class maximumProduct_leet(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = [float('-inf')] * 3
        mini = [float('inf')] * 3
        for n in nums:
            if n < mini[0]:
                mini = [n, mini[0]]
            elif n < mini[1]:
                mini = [mini[0], n]

            if n > maxi[0]:
                maxi = [n, maxi[0], maxi[1]]
            elif n > maxi[1]:
                maxi = [maxi[0], n, maxi[1]]
            elif n > maxi[2]:
                maxi = [maxi[0], maxi[1], n]

        return max(mini[0]*mini[1]*maxi[0],maxi[0]*maxi[1]*maxi[2])
if __name__ == "__main__":
    a = [-6,-2,1,2,3,4]  #output=24

    x = maximumProduct_leet()
    print x.maximumProduct(a)