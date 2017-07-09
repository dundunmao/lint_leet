# -*- encoding: utf-8 -*-
# 3级
# 内容:假设一个sorted array 在某个pivot上rotated,例如( 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2)可以有duplicate,找到最小数.
# 方法:每次取中间,如果中间的比头的大,说明前半块从小到大排列,那小的应该在后半段,头就放在中间
def findMin(self, nums):
    beg = 0
    end = len(nums)-1
    while beg <= end:
        while beg < end and nums[beg] == nums[beg + 1]:  #这两个while解决 duplicate的问题
            beg += 1
        while end > beg and nums[end] == nums[end - 1]:
            end -= 1
        if beg == end:
            return nums[beg]

        mid = (beg+end)/2
        if nums[mid] > nums[end]:
            beg = mid + 1
        else:
            end = mid


    return nums[beg]