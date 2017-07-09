# coding:utf-8
# 题目:给一个数组[2,3,1,2,4,3]和一个数7,问最短的sumarray的长度that sum >= 7 的


# 4two_pointer,头一个指针left,尾一个指针right,从头开始叠加,发现到比7大了,算头尾的距离,记录下来,
# 在让left往下走,直到sum不大于7了,再让right往下走,在left走,每次都记录距离,取距离最小那个.

def minSubArrayLen1(s, nums):
    total = left = 0
    result = len(nums) + 1
    for right, n in enumerate(nums): #列举enumerate(nums) = [(0,2),(1,3),(2,1),(3,2),(4,4),(5,3)]
        total += n #right指针往下走
        while total >= s:
            distance = right - left + 1
            result = min(result, distance) #存的是最小的符合条件的距离
            total -= nums[left] #left指针往下走
            left += 1
    return result if result <= len(nums) else 0



# binary search

class Solution:

    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):# 计数从1开始[(1,3),(2,1),(3,2),(4,4),(5,3)]
            nums[idx] = nums[idx - 1] + n #这个位置的数等于他前面所有数之和
        left = 0
        for right, n in enumerate(nums):#这时的nums是求和之后的新list
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    s = 7
    print minSubArrayLen1(s, nums)