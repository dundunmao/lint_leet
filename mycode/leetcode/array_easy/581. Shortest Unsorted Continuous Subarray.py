# -*- encoding: utf-8 -*-
# 题目：给一个array： [2, 6, 4, 8, 10, 9, 15] 找出一个subarray使得只要把subarray排序，这个数组就排序了，求这个subarray的长度
# 解题：
class Solution(object):
    # Time Limit Exceeded
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    start = i
                    flag = True
                    break
            if flag == True:
                break
        flag = False
        if i == len(nums) - 1:
            return 0
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1 ,-1):
                if nums[j] > nums[i]:
                    end = i
                    flag = True
                    break
            if flag == True:
                break
        return end - start + 1
#找到第一个上凸点和最后一个下凹点
    class Solution(object):
        def findUnsortedSubarray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            n = len(nums)
            start = -1
            end = -2
            mini = nums[n - 1]
            maxi = nums[0]
            for i in range(1, n):
                maxi = max(maxi, nums[i])
                mini = min(mini, nums[n - 1 - i])
                if nums[i] < maxi:  # 如果nums[i]在这里没被更新，说明他就是要找那个
                    end = i  # 不断更新，找最后一个下凹点
                if nums[n - 1 - i] > mini:  # 如果nums[n-1-i]在这里没被更新，说明他就是要找那个
                    start = n - 1 - i  # 不断更新，找第一个上凸点
            return end - start + 1


if __name__ == "__main__":
    a = [2,6,4,8,10,9,15]
    x = Solution()
    print x.findUnsortedSubarray_daan(a)