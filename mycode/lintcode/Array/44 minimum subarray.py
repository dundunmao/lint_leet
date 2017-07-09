
# -*- encoding: utf-8 -*-
class Solution:
    def minSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
        nums_in = [-x for x in nums]
        pre_sum = 0
        min_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums_in)):
            pre_sum += nums_in[i]
            max_sum = max(max_sum, pre_sum-min_sum)
            min_sum = min(min_sum, pre_sum)
        return -max_sum
    def minSubArray2(self,nums):
        if nums is None or len(nums) == 0:
            return None
        length = len(nums)
        localmin = [0]*length
        globalmin = [0]*length
        for j in range(length):
            if j == 0:
                globalmin[j] = localmin[j] = nums[j]
            else:
                localmin[j] = min(localmin[j-1]+nums[j], nums[j])
                globalmin[j] = min(globalmin[j-1], localmin[j])
        return globalmin[length-1]
    def minSubArray3(self,nums):
        local_min = 0
        global_min = float('inf')
        for i in range(len(nums)):
            local_min = min(local_min+nums[i], nums[i])
            global_min = min(global_min, local_min)
        return global_min

#我的练习
class Solution1:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
        # initial
        prefix = 0
        min_subarray = float('inf')
        max_pre = 0
        # main part: for loop
        for i in range(len(nums)):
            prefix += nums[i]
            min_subarray = min(min_subarray, prefix - max_pre)
            print min_subarray
            max_pre = max(max_pre, prefix)
        return min_subarray


    def min_sub(self, nums):
        result = [0]
        max_prefix = 0
        min_sub = float('inf')
        prefix = 0
        for i in range(0, len(nums)):
            prefix += nums[i]
            min_sub = min(min_sub, prefix - max_prefix)
            result.append(min_sub)
            max_prefix = max(max_prefix, prefix)
        return result

if __name__ == "__main__":

    A = [1,2,-3,1]

    s = Solution1()

    print s.min_sub(A[::-1])