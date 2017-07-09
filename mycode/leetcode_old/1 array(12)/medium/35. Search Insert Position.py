# coding:utf-8
# 给定一个sorted list和一个数,如果这个数找到了就return index,如果没找到就按大小插入进去,并返回index

class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:  #如果在里面
            return nums.index(target)
        elif target<nums[0]: #如果比第一个数小,
            return 0

        elif target >nums[-1]:#如果比最后一个数大
            return len(nums)
        else:               #二分法
            left = 0
            right = len(nums)-1
            while left<right-1:
                mid = (left+right)//2
                if target<nums[mid]:
                    right = mid
                else:
                    left = mid
        return left+1


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 2
    s = Solution()
    print s.searchInsert(nums,target)