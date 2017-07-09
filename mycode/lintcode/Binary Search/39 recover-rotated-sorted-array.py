# -*- encoding: utf-8 -*-
# 给定一个旋转排序数组，在原地恢复其排序。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# 什么是旋转数组？
#
# 比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
# 样例
# [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
        # find biggest num
        l = len(nums)
        start = 0
        end = l-1
        peak = 0
        while start+1 < end:
            mid = start + (end-start)/2
            if nums[mid]<=nums[l-1]: # lower part
                end = mid
            else:    # upper part
                start = mid
        if nums[start]>nums[end]:
            peak = start
        else:
            peak = end
        return nums[peak+1:]+nums[:peak+1]


if __name__ == "__main__":
    nums = [4, 5, 1, 2, 3]
    s = Solution()
    print s.recoverRotatedSortedArray(nums)