# coding:utf-8
# 3级
# 题目:在rotated sorted array(例如 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2)里找到最小值.
# binary search
def findMin(nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            m = (i+j) / 2
            if nums[m] > nums[j]:   #如果尾值比中值小,说明最小值在后一半
                i = m + 1
            else:                   #反之,在前一半
                j = m
        return nums[i]
if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    print findMin(nums)