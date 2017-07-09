# coding:utf-8
# 3级
# 题目 integer list,问有没有其中4个数相加等于target的 (a ≤ b ≤ c ≤ d,且list无重复)
# 思路 跟39题像.用recursive的方法,
#
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:   #如果总长小于要取的数,或者要取的数小于2
            return

        # solve 2-sum
        if N == 2:                  #如果要取的数等于2
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:                       #其他情况
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # 因为是sorted的,target比第一个数的N倍小,那任意N个数的和都会比target大;target比最后一个数的n倍大,那也找不到四个数的合为N了
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N(防止有重复情况)
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results) #等于第i个数+后面的数中任取N-1个合为target-nums[0]
        return