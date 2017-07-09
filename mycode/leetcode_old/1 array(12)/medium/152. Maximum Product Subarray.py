# coding:utf-8
# 3级
# 题目:Find the contiguous subarray within an array (containing at least one number) which has the largest product.求乘积最大的连续子数组
#     例如:list=[2,3,-2,4],the contiguous subarray [2,3] has the largest product = 6.
# 思路
def maxProduct(nums):
    MinTemp = nums[0]
    MaxTemp = nums[0]
    Max = nums[0]
    for i in xrange(1, len(nums)):
        print nums[i],nums[i] * MaxTemp,nums[i] * MinTemp
        # Min记录的是最大的负数或最小的正数,Max记录的是最大的正数或最小的负数.防止后面有负数乘进去
        MinTemp, MaxTemp = min(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp), max(nums[i], nums[i] * MaxTemp, nums[i] * MinTemp)
        Max = max(Max, MaxTemp)
    return Max

if __name__ == '__main__':
    nums =[2,3,-2,-4,7]
    print maxProduct(nums)