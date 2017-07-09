# -*- encoding: utf-8 -*-
# Partition an unsorted integer array into three parts:
# The front part < low
# The middle part >= low & <= high
# The tail part > high
# Return any of the possible solutions.
#
#  注意事项：low <= high in all testcases.
# 样例
# Given [4,3,4,1,2,3,1,2], and low = 2 and high = 3.
#
# Change to [1,1,2,3,2,3,4,4].
#
# ([1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not)
#
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, low, high):
        if nums is None or len(nums) <= 1:
            return
        le = len(nums)
        l = 0
        r = le - 1
        i = 0
        while i <= r:
            if nums[i] < low:
                nums[i],nums[l] = nums[l],nums[i]
                l += 1
                i += 1
            elif nums[i] > high:
                nums[i],nums[r] = nums[r],nums[i]
                r -= 1
            else:
                i += 1
        return nums
if __name__ == '__main__':
    list = [4,3,4,1,2,3,1,2]
    low = 2
    high = 3
    s = Solution()
    print s.partitionArray(list, low, high)