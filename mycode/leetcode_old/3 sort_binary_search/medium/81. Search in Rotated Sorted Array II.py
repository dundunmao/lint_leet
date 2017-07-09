# coding:utf-8
# 3级
# 题目:sorted但是rotate的list,比如[4,5,6,7,0,1,2]找一个target比如0.要考虑有重复的元素
#思路,就要要binary search,
def search(nums, target):
    print nums
    if target not in nums:
        return -1
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (high+low)//2
        print nums[low], nums[mid],nums[high]
        if target == nums[mid]:
            return True
        ################# before is the same as original one ###############
        while low < mid and nums[low] == nums[mid]: # tricky part
            low += 1                #为了把重复的前端去掉
        ################# after is the same as original one ###############
        # the first half is ordered
        if nums[low] <= nums[mid]:
            # target is in the first half
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # the second half is ordered
        else:
            # target is in the second half
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False

if __name__ == '__main__':
    nums = [13,13,14]
    target = 14
    print  search(nums, target)