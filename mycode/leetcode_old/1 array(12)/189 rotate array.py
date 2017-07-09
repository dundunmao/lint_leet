# -*- encoding: utf-8 -*-
# 2级
# 内容：（n,k）把n长度的array 后面的数往前放，做k次(in place)
# 思路:用 insert(nums[-1]) 和 pop


def rotate(nums, k):
    if nums == []:
        nums = []
    else:
        for i in range(0,k):
            nums.insert(0,nums.pop())
    return nums



if __name__ =="__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print rotate(nums,k)