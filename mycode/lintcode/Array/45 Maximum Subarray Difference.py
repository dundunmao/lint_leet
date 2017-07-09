# -*- encoding: utf-8 -*-
# 给定一个整数数组，找出两个不重叠的子数组A和B，使两个子数组和的差的绝对值|SUM(A) - SUM(B)|最大。
#
# 返回这个最大的差值。
#
#  注意事项
#
# 子数组最少包含一个数
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数组[1, 2, -3, 1]，返回 6
# 这题就是遍历i,走到一个位置,找到max_left-min_right和max_right-min_left.最后求所有中的最大
# 这题是前面几题 的综合,麻烦的地方在于位置要对齐.
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        A1 = self.max_subarray(nums)
        B1 = self.min_subarray(nums)
        max_dif1 = float('-inf')
        for i in range(1,len(nums)):
            max_dif1 = max(max_dif1, A1[i]-B1[i-1])
        nums.reverse()
        A2 = self.max_subarray(nums)
        B2 = self.min_subarray(nums)
        max_dif2 = float('-inf')
        for i in range(1,len(nums)):
            max_dif2 = max(max_dif2, A2[i]-B2[i-1])
        return max(max_dif1, max_dif2)



    def min_subarray(self, nums):
        if len(nums) == 1:
            return nums[0]
        local_min = 0
        global_min = float('inf')
        min_array = [0]*len(nums)
        for k in range(len(nums)):
            local_min = min(local_min+nums[k], nums[k])
            global_min = min(global_min, local_min)
            min_array[k] = global_min
        return min_array

    def max_subarray(self, nums):
        if len(nums) == 1:
            return nums[0]
        local_max = 0
        global_max = float('-inf')
        max_array = [0]*len(nums)
        for j in range(len(nums))[::-1]:
            local_max = max(local_max+nums[j], nums[j])
            global_max = max(global_max, local_max)
            max_array[j] = global_max
        return max_array

#我的练习
class Solution1:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        # from left to right
        max_left = self.max_sub(nums)
        print max_left
        min_right = self.min_sub(nums[::-1])
        print min_right
        result_left = 0
        for i in range(0,len(nums)-1):
            result_left = max(result_left,abs(max_left[i] - min_right[-i-2]))

        # from right to left
        max_right = self.max_sub(nums[::-1])
        print max_right
        min_left = self.min_sub(nums)
        print min_left
        result_right = 0
        for i in range(0,len(nums)-1):
            result_right = max(result_right,abs(min_left[i] - max_right[-i-2] ))
        return max(result_left, result_right)



    def max_sub(self, nums):
        result =[]
        min_prefix = 0
        max_sub = float('-inf')
        prefix = 0
        for i in range(0,len(nums)):
            prefix += nums[i]
            max_sub = max(max_sub, prefix - min_prefix)
            result.append(max_sub)
            min_prefix = min(min_prefix, prefix)
        return result


    def min_sub(self, nums):
        result =[]
        max_prefix = 0
        min_sub = float('inf')
        prefix = 0
        for i in range(0,len(nums)):
            prefix += nums[i]
            min_sub = min(min_sub, prefix - max_prefix)
            result.append(min_sub)
            max_prefix = max(max_prefix, prefix)
        return result
if __name__ == "__main__":

    A = [-5,-4]
    # A = [1, -3, 2, 1]

    s = Solution1()


    print s.maxDiffSubArrays(A)