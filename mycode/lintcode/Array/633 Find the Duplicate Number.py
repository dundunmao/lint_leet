# -*- encoding: utf-8 -*-
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# n+1个整数的数组，从1-n里出，证明至少存在一个duplicate
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
#


#  index方法
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                return index+1
# 二分法
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) / 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low

# linked list cycle ii方法
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1: #保证有两个数以上
            slow = nums[0]
            fast = nums[nums[0]]

            # Keep advancing 'slow' by one step and 'fast' by two steps until they
            # meet inside the loop.
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            # Start up another pointer from the end of the array and march it forward
            # until it hits the pointer inside the array.
            fast = 0
            while fast != slow:
                fast = nums[fast]
                slow = nums[slow]

            return slow
        return -1
if __name__ == "__main__":

    A = [1,2,3,3,4,5]
    s = Solution()

    print s.findDuplicate(A)