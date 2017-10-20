# -*- encoding: utf-8 -*-
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
# Given [5, 4, 3, 2, 1],
# return false.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small,big = float('inf'),float('inf')
        for ele in nums:
            if ele <= small:
                small = ele
            elif ele <= big:
                big = ele
            else:
                return True
        return False

# DP 超时
class Solution1(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i],f[j]+1)
            # if nums[i] > nums[i-1]:
            #     f[i] = f[i - 1] + 1
                if f[i] >= 3:
                    return True
        return False
if __name__ == '__main__':
    a = [3,5,2,6]
    s = Solution()
    s.increasingTriplet(a)