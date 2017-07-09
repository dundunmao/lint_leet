# -*- encoding: utf-8 -*-
# 1级
# 内容:Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 主要方法:
def merge(nums1, m, nums2, n):
    nums3 = nums1[:m]+nums2[:n]
    nums3.sort()
    nums1[:m+n] = nums3  #因为需要 in place
    return nums1


if __name__ =="__main__":
    nums1 = [0,1,1,3]
    nums2 = [0.5,4,5,5,5,1]
    m = 2
    n = 3
    print merge(nums1, m, nums2, n)