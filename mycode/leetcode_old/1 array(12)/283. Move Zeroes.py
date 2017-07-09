# -*- encoding: utf-8 -*-
# 2级
# 内容：把0都移后面去，其他的前移(in place)
# 思路：两个指针,


def moveZeroes(nums):
    length = len(nums)
    i,j = 0,0
    while i<length and j<length:
        if nums[i]!= 0:
            nums[j] = nums[i]
            i+=1
            j+=1
        else:
            i+=1
    while j<length:
        nums[j] = 0
        j+=1

if __name__ == '__main__':
    nums = [0,1,2,0,9,8,0,7,0]
    print moveZeroes(nums)
