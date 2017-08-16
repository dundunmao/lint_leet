# coding:utf-8
# 跟进“搜索旋转排序数组”，假如有重复元素又将如何？
#
# 是否会影响运行时间复杂度？
#
# 如何影响？
#
# 为何会影响？
#
# 写出一个函数判断给定的目标值是否出现在数组中。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出[3,4,4,5,7,0,1,2]和target=4，返回 true
# 思路，就是把前后重复的点都去掉，去之前check是不是target。这样就不怕都去掉了
class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """
    def search(self, A, target):
        # write your code here
        if A is None or target is None or len(A) == 0:
            return False
        start = 0
        l = len(A)
        end = l - 1
        flag = A[start]
        if A[start] == A[end]:
            if target == A[start]:
                return True
            else:
                while A[start] == A[end]:
                    start+=1
                    end-=1
        while start + 1 < end:
            mid = start+(end-start)/2
            if target == A[end]:
                return True
            elif target < A[end]:
                if A[mid] == target:
                    return True
                elif A[mid] < target:
                    start = mid
                else:
                    if A[mid]> target:
                        end = mid
                    else:
                        start = mid
            else:
                if A[mid]==target:
                    return True
                elif A[mid]>target:
                    end = mid
                else:
                    start = mid
        if A[start] == target:
            return True
        elif A[end] == target:
            return True
        else:
            return False

    def search_leetcode(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        l = len(nums)
        start = 0
        end = l - 1
        if nums[start] == nums[end]:
            if nums[start] == target:
                return True
            while nums[start] == nums[end] and start < end:
                start += 1
        if target <= nums[l - 1]:
            while start + 1 < end:
                mid = (start + end) / 2
                if nums[mid] > nums[l - 1]:
                    start = mid
                else:
                    if target == nums[mid]:
                        return True
                    elif target > nums[mid]:
                        start = mid
                    elif target < nums[mid]:
                        end = mid
        else:
            while start + 1 < end:
                mid = (start + end) / 2
                if nums[mid] <= nums[l - 1]:
                    end = mid
                else:
                    if target == nums[mid]:
                        return True
                    elif target < nums[mid]:
                        end = mid
                    else:
                        start = mid

        if nums[start] == target:
            return True
        elif nums[end] == target:
            return True
        return False