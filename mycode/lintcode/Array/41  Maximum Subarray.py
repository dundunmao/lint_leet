# -*- encoding: utf-8 -*-
# 给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。
#
#  注意事项
#
# 子数组最少包含一个数字
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组[1, -1, -2, 1]，返回 -3
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """


    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        min_prefix = 0
        max_subarray = float('-inf')
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            max_subarray = max(max_subarray, prefix - min_prefix)#遍历到的pre_sum减去最小的pre_sum得到的就是这一轮的最大sum
            min_prefix = min(min_prefix, prefix)# 记录最小的pre_sum,要在算完max之后再更新,因为这里的min是上一次的(max_subarray= prefix[j]-prefix[i]), i 是j前面的.
        return max_subarray

    def maxSubArray2(self,nums):
        local_max = 0
        global_max = float('-inf')
        for i in range(len(nums)):
            local_max = max(local_max+nums[i], nums[i])  #因为local_max+nums[i]<nums[i],所以local_max<0.累计的这一段小于0,就不能要他了.
            global_max = max(global_max, local_max)
        return global_max

    def maxSubArray_leet(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case
        if nums is None or len(nums) == 0:
            return 0
        pre_sum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            pre_sum.append(sum)
        mini = 0
        maxi = float('-inf')
        for i in range(len(nums)):
            maxi = max(maxi,pre_sum[i] - mini)
            mini = min(mini, pre_sum[i])
        return maxi
if __name__ == "__main__":

    # A = [-2, 2, -3,4,-1,2,1,-5,3]
    A = [1,2,3]
    s = Solution()

    print s.maxSubArray3(A)