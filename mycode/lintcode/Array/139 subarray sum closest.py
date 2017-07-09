# coding:utf-8
# 给定一个整数数组，找到一个和最接近于零的子数组。返回第一个和最有一个指数。你的代码应该返回满足要求的子数组的起始位置和结束位置
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出[-3, 1, 1, -3, 5]，返回[0, 2]，[1, 3]， [1, 1]， [2, 2] 或者 [0, 4]。
#

class pair():
    def __init__(self, value, index):
        self.value = value
        self.index = index
class Solution:

    def subarraySumClosest(self, nums):
        result = []
        # edge case
        if nums is None:
            return result
        length = len(nums)
        if length == 1:
            return [0,0]
        pre_sum_array = [pair(0,0)]
        prev = 0 # dummy node
        for i in range(1,length+1):
            pre_sum_array.append(pair(prev+nums[i-1], i))
            # prev = pre_sum_array[i].value
            prev += nums[i-1]
        mini = float('inf')
        pre_sum_array = sorted(pre_sum_array, key=lambda pair: pair.value)
        for i in range(1,length+1):
            if mini > pre_sum_array[i].value - pre_sum_array[i-1].value:
                mini = pre_sum_array[i].value - pre_sum_array[i-1].value
                result = []
                tmp = [pre_sum_array[i].index - 1, pre_sum_array[i - 1].index - 1]
                tmp.sort()
                result.append(tmp[0] + 1)
                result.append(tmp[1])
        return result

# 我的练习
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        res = []
        if not nums:
            return res
        prefix_sum = 0
        array = [(0,0)]
        for i in range(0, len(nums)):
            prefix_sum += nums[i]
            array.append((i+1,prefix_sum))
        pre_sum_sort = sorted(array,key=lambda d: d[1] )
        diff = float('inf')
        for i in range(1,len(pre_sum_sort)):
            abs_diff = abs(pre_sum_sort[i][1] - pre_sum_sort[i - 1][1])
            if diff > abs_diff:
                diff = abs_diff
                result = [pre_sum_sort[i-1][0]-1,pre_sum_sort[i][0]-1]

        result.sort()
        result[0] = result[0]+1
        return result

if __name__ == "__main__":


    A = [5,10,5,3,2,1,1,-2,-4,3]

    s = Solution1()

    print s.subarraySumClosest(A)