# coding:utf-8
# 3级
# 题目:peak element就是他比他邻居大,给一个相邻元素不相等的list,(可能有多个peak,return一个就行)其中可以认为num[-1] = num[n] = -∞
# 例如:in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
# 解题:取中间点,如果中间点比左右都高,return中间点.如果右边高,就取右边这半(这半肯定有peak)
#  if an element(not the right-most one) is smaller than its right neighbor, then there must be a peak element on its right,
#  because the elements on its right is either
#    1. always increasing  -> the right-most element is the peak
#    2. always decreasing  -> the left-most element is the peak
#    3. first increasing then decreasing -> the pivot point is the peak
#    4. first decreasing then increasing -> the left-most element is the peak
#    Therefore, we can find the peak only on its right elements( cut the array to half)
#
#    The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.
#
# Conditions:
#      1. array length is 1  -> return the only index
#      2. array length is 2  -> return the bigger number's index
#      3. array length is bigger than 2 ->
#            (1) find mid, compare it with its left and right neighbors
#            (2) return mid if nums[mid] greater than both neighbors
#            (3) take the right half array if nums[mid] smaller than right neighbor
#            (4) otherwise, take the left half

def findPeakElement(nums):
    left = 0
    right = len(nums)-1

    # handle condition 3
    while left < right-1:
        mid = (left+right)/2                                    #取中间点
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:  #如果中间点比左右都高,return中间点
            return mid

        if nums[mid] < nums[mid+1]:                             #如果中间点比右边矮,取右边一半
            left = mid+1
        else:                                                   #反之亦然
            right = mid-1

    #handle condition 1 and 2
    return left if nums[left] >= nums[right] else right         #最后剩两个数,取left如果left大,反之亦然




#O(N)不符合题意,题意要O(lg(n))
def findPeakElement(nums):

    for i in range(1,len(nums)-1):
        # for j in range(i+1,len(nums)):
        if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
            return i






if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print findPeakElement(nums)
