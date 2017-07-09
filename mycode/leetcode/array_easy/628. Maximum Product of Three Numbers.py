
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