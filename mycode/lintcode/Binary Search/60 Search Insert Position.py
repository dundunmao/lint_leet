# coding:utf-8

# 给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
#
# 你可以假设在数组中无重复元素。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# [1,3,5,6]，5 → 2
#
# [1,3,5,6]，2 → 1
#
# [1,3,5,6]， 7 → 4
#
# [1,3,5,6]，0 → 0
#

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A == []:
            return 0
        if A is None or target is None:
            return False
        if target == '':
            return 0
        start = 0
        #  remember "-1", otherwise index out of range
        end = len(A) - 1
        # not "start<end"
        while start + 1 < end:
            # not "(end+start)/2", since if start, end -> 2^31-1 out of range
            medium = start + (end-start)/2
            if target < A[medium]:
                end = medium
            if target == A[medium]:
                return medium
            if target > A[medium]:
                start = medium
        # start,end adjaction or equals all regart adjaction
        if target <= A[start]:
            return start
        elif target <= A[end]:
            return end
        elif target > A[end]:
            return end+1

if __name__ == "__main__":
    A = [1, 3, 5, 6]
    target = 5
    s = Solution()
    print s.searchInsert(A,target)