# -*- encoding: utf-8 -*-
# 给定一个整数数组，找出两个 不重叠 子数组使得它们的和最大。
# 每个子数组的数字在数组中的位置应该是连续的。
# 返回最大的和。
#
#  注意事项
#
# 子数组最少包含一个数
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组 [1, 3, -1, 2, -1, 2]
# 这两个子数组分别为 [1, 3] 和 [2, -1, 2] 或者 [1, 3, -1, 2] 和 [2]，它们的最大和都是 7
class Solution:
    def maxTwoSubArrays(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        sum_left = 0
        sum_right = 0
        max_left = float('-inf')
        max_right = float('-inf')
        min_left = 0
        min_right = 0
        left = [0]*len(nums)
        right = [0]*len(nums)
        for k in range(len(nums)):
            sum_left += nums[k]
            max_left = max(max_left, sum_left - min_left)
            min_left = min(min_left, sum_left)
            left[k] = max_left
        for j in range(len(nums))[::-1]:
            sum_right += nums[j]
            max_right = max(max_right, sum_right-min_right)
            min_right = min(min_right, sum_right)
            right[j] = max_right
        max_two = float('-inf')
        for l in range(len(nums)-1):
            sum = left[l]+right[l+1]
            max_two = max(max_two, sum)
        return max_two
# 我的练习
class Solution2:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        sum_total = sum(nums)
        result = float('-inf')
        for i in range(1, len(nums)):
            result = max(result, self.max_sum(nums[:i]) + self.max_sum(nums[i:]))
        return max(sum_total, result)

    def max_sum(self, a):
        if len(a) == 0:
            return 0
        pre_sum = []
        sum = 0
        for i in range(len(a)):
            sum += a[i]
            pre_sum.append(sum)
        mini = 0
        maxi = float('-inf')
        for i in range(len(a)):
            maxi = max(maxi, pre_sum[i] - mini)
            mini = min(mini, pre_sum[i])
        return maxi

if __name__ == "__main__":

    A = [1,3,-1,2,-1,2]

    s = Solution()

    print s.maxTwoSubArrays(A)