# coding:utf-8
# 给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。
#
# 如果目标值不在数组中，则返回[-1, -1]
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出[5, 7, 7, 8, 8, 10]和目标值target=8,
#
# 返回[3, 4]
#

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if A is None or target is None or len(A) == 0:
            return [-1, -1]
        start = 0
        end = len(A) - 1
        # 14 find first position of target
        while start + 1 < end:
            mid = (start + end) / 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        # "start" first
        if A[start] == target:
            leftBound = start
        elif A[end] == target:
            leftBound = end
        else:
            return [-1, -1]
        # 458 last position of target
        start, end = leftBound, len(A) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            # contain "="
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        # "end" first
        if A[end] == target:
            rightBound = end
        else:
            rightBound = start
        return [leftBound, rightBound]
    def searchRange_leet(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return [-1,-1]
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            first = start
        elif nums[end] == target:
            first = end
        else:
            return [-1,-1]
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            second = end
        elif nums[start] == target:
            second = start
        else:
            return [-1,-1]
        return [first,second]
if __name__ == "__main__":
    A = [1,3]
    t = 1
    s = Solution()
    print s.searchRange_leet( A, t)