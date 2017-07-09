# coding:utf-8
# 假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。
#
# 你可以假设数组中不存在重复的元素。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出[4, 5, 1, 2, 3]和target=1，返回 2
#
# 给出[4, 5, 1, 2, 3]和target=0，返回 -1
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        l = len(A)
        if A is None or l == 0 or target is None:
            return -1
        start = 0
        end = l-1
        while start + 1 < end:
            mid = start + (end - start)/2
            if target == A[l-1]:
                return l-1
            elif target > A[l-1]:
                if A[mid] == target:
                    return mid
                elif A[mid] > target:
                    end = mid
                else:
                    if A[mid] < A[start]:
                        end = mid
                    else:
                        start = mid
            else:
                if A[mid] == target:
                    return mid
                elif A[mid] < target:
                    start = mid
                else:
                    if A[mid] > A[end]:
                        start = mid
                    else:
                        end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1


class Solution2:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        l = len(A)
        if A is None or l == 0 or target is None:
            return -1
        start = 0
        end = l-1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if target == A[end]:
                return end
            elif target > A[end]:
                if A[mid] > A[end]:
                    if target > A[mid]:
                        start = mid
                    elif target < A[mid]:
                        end = mid
                    else:
                        return mid
                else:
                    end = mid
            else:
                if A[mid] > A[end]:
                    start = mid
                else:
                    if target > A[mid]:
                        start = mid
                    elif target < A[mid]:
                        end = mid
                    else:
                        return mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1

    def search_leetcode(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        l = len(nums)
        start = 0
        end = l - 1
        if target <= nums[l - 1]:
            while start + 1 < end:
                mid = (start + end) / 2
                if nums[mid] > nums[l - 1]:
                    start = mid
                else:
                    if target == nums[mid]:
                        return mid
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
                        return mid
                    elif target < nums[mid]:
                        end = mid
                    else:
                        start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1
if __name__ == "__main__":

    target = 8
    s = Solution2()
    print s.search(nums,target)