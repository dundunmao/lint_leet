# -*- encoding: utf-8 -*-
# 给出一个整数数组 nums 和一个整数 k。划分数组（即移动数组 nums 中的元素），使得：
#
# 所有小于k的元素移到左边
# 所有大于等于k的元素移到右边
# 返回数组划分的位置，即数组中第一个位置 i，满足 nums[i] 大于等于 k。
#
#  注意事项：你应该真正的划分数组 nums，而不仅仅只是计算比 k 小的整数数，如果数组 nums 中的所有元素都比 k 小，则返回 nums.length。
#

# 给出数组 nums = [3,2,2,1] 和 k = 2，返回 1.

#解题： 要时刻检查i是不是在j的前面，不然互换就错了
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if nums is None:
            return None
        i = 0
        j = len(nums)-1
        while i<=j:
            while i<=j and nums[i]<k:   #要时刻检查i是不是在j的前面，不然互换就错了
                    i += 1
            while i<=j and nums[j]>=k:
                    j -= 1
            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j-=1
        return j+1
# 我的方法不好，这题要时刻警惕i在j的后面
class Solution_self:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if nums is None:
            return None
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums)-1
        while i<=j:
            while i < len(nums) and nums[i] < k:
                i += 1
                if i == len(nums):
                    return i
            while j >= 0 and nums[j] >= k:
                j -= 1
                if j == -1:
                    return 0
            nums[i],nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        if nums[i] >= k:
            return i
        else:
            return i + 1
if __name__ == '__main__':

    list = [9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9]
    k = 9
    s = Solution_self()
    print s.partitionArray(list,k)