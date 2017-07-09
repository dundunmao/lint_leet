# coding:utf-8
# 题目:sorted但是rotate的list,比如[4,5,6,7,0,1,2]找一个target比如0.
#思路,就要要binary search,
# 用mid = (low+high)/2; high=mid-1; low=mid+1,这样的方程最后让low,mid,high,target集中在一个sorted 范围里让mid=target
# 如果是边缘的,最后可能是0,0,0
def search(nums, target):
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) / 2
        print nums[low], nums[mid],nums[high]
        if target == nums[mid]:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

if __name__ == '__main__':
    nums = [7,8,9,10,11,12,13,14,1,2,3]
    target = 14

    print  search(nums, target)
