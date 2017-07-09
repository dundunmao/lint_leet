# coding:utf-8
# 题目:Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
#思路:正sorted一下,反sorted一下,然后按顺序互相插入

def wiggle_sort(nums):
    s1 = sorted(nums)
    s2 = sorted(nums, reverse = True)
    for i in range(len(nums)/2):
        nums[i*2] = s1[i]
        nums[i*2+1] = s2[i]


    return nums

if __name__ == '__main__':
    nums = [3, 5, 2, 1, 6, 4]
    print wiggle_sort(nums)