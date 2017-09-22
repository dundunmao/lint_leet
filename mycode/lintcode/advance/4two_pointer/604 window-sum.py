

# 给你一个大小为n的整型数组和一个大小为k的滑动窗口，将滑动窗口从头移到尾，输出从开始到结束每一个时刻滑动窗口内的数的和。
class Solution:
    """
    @param: nums: a list of integers.
    @param: k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if nums == []:
            return []
        if len(nums) <= k:
            return [sum(nums)]

        temp = sum(nums[:k])
        res = [temp]
        array = nums[:k]
        j = 0
        for i in range(k ,len(nums)):
            temp -= nums[j]
            j += 1
            temp += nums[i]
            res.append(temp)
        return res
