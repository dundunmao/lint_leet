# -*- encoding: utf-8 -*-
# 给定一组数组arrays，各数组递增有序，求不同数组之间最小值、最大值之间差值绝对值的最大值。# Input:
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4

class Solution_leet(object):
    def distributeCandies(self, nums):
        maxi = nums[0][-1]
        mini = nums[0][0]
        ans = 0
        for i in range(1,len(nums)):
            ans = max(ans,abs(nums[i][-1] - mini),abs(nums[i][0] - maxi))
            mini = nums[i][0]
            maxi = nums[i][-1]
        return ans

if __name__ == "__main__":
    nums = [[1,2,3],[4,5],[1,2,3]]
    x = Solution_leet()
    print x.distributeCandies(nums)