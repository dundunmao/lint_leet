# -*- encoding: utf-8 -*-
# Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
# Examples:
#
#   Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
#   Output: 6  (j = 7, i = 1)
#
#   Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
#   Output: 8 ( j = 8, i = 0)
#
#   Input:  {1, 2, 3, 4, 5, 6}
#   Output: 5  (j = 5, i = 0)
#
#   Input:  {6, 5, 4, 3, 2, 1}
#   Output: -1
class Solution(object):
    def maxIndexDiff(self, nums):
        le = len(nums)
        l_min = [nums[0]]
        # l_min 每个数存的是从左数最小的数
        for i in range(1,le):
            l_min.append(min(nums[i],l_min[i - 1]))
        r_max = [None for i in range(le)]
        r_max[-1] = nums[-1]
        # r_max 每个数存的是从右数最大的数
        for i in range(le - 2,-1,-1):
            r_max[i]= max(nums[i],r_max[i + 1])
        i = 0
        j = 0
        max_diff = -1
        # l_min =[34, 8, 8, 3, 2, 2, 2, 2, 1]
        # r_max =[80, 80, 80, 80, 80, 80, 33, 33, 1]
        # 相当于锁住一个i，让j往后走，找到从右往左第一个比i大的数，更新这个距离
        # 当不能再大了，i往后走，j再继续往后找
        while j < le and i < le:
            if l_min[i] < r_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1
            else:
                i += 1
        return max_diff

if __name__ == "__main__":
    a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    x = Solution()
    print x.maxIndexDiff(a)