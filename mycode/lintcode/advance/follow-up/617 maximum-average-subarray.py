# -*- encoding: utf-8 -*-
class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        # Write your code here
        if nums is None:
            return None
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        l = min(nums)
        r = max(nums)
        n = len(nums)
        pre_sum = [0 for _ in range(n+1)]
        while r - l >= 1e-6:
            mid = (l+r)/2.0 #二分找x
            check = False  #是否存在这么一段

            min_pre = 0
            for i in range(1,n+1):
                # A[i] - x
                pre_sum[i] = pre_sum[i-1] + nums[i -1] - mid
                # 要表达是否存在一段 pre_sum[i] - pre_sum[j-1] >= 0 and j<= i-k+1
                # 这里min_pre 是pre_sum[j-1]在j<= i-k+1范围内的最小值
                if pre_sum[i] - min_pre >= 0 and i >= k:
                    check = True
                    break
                if i >= k:
                    min_pre = min(min_pre, pre_sum[i - k + 1]) #随着i的增加，不断的维护这个j的最小值
            if check:  #如果存在，就把这个mid加大
                l = mid
            else:      #如果不存在，说明不存在这个x，要把x变小
                r = mid
        return l
if __name__ == "__main__":
    s = Solution()
    A = [1,12,-5,-6,50,3]
    k = 3
    print s.maxAverage(A,k)
