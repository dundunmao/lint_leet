# coding:utf-8

# 给定一个整数数组，找到和为零的子数组。你的代码应该返回满足要求的子数组的起始位置和结束位置
#
#  注意事项
#
# There is at least one subarray that it's sum equals to zero.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 [-3, 1, 2, -3, 4]，返回[0, 2] 或者 [1, 3].
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        pre_sum_array = [0]
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            pre_sum_array.append(pre_sum)
        dic = {}
        for i in range(len(pre_sum_array)):
            if dic.has_key(pre_sum_array[i]):
                dic[pre_sum_array[i]].append(i-1)
                return dic[pre_sum_array[i]]
            else:
                dic[pre_sum_array[i]] = [i]
# 我的练习 hash 方法
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        # edge case
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            if nums[0] == 0:
                return[0,0]
            else:
                return None
        # initialize
        le = len(nums)
        presum = 0
        hash = {}
        hash[0] = 0
        for i in range(0,le):
            presum += nums[i]
            if hash.has_key(presum):
                return[hash[presum],i]
            else:
                hash[presum] = i+1

        return None
# 我的练习 DP方法
# Memory Limit Exceeded
class Solution2:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        # edge case
        if nums is None or len(nums) == 0:
            return None
        if len(nums) == 1:
            if nums[0] == 0:
                return[0,0]
            else:
                return None
        # initialize
        # f[x][y] is sum from nums[i] to nums[j]
        m = len(nums)
        f = [[0 for i in range(m)] for j in range(m)]
        f[0][0] = nums[0]

        # dp
        for i in range(0,m):
            for j in range(i,m):
                f[i][j] = f[i][j-1] + nums[j]
                if f[i][j] == 0:
                    return[i,j]
        return None

class Solution_leet(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        return有多少个符合条件的subarray,而不是subarray里的元素个数
        """
        if nums is None or len(nums) == 0:
            return 0
        pre_sum = [0]
        s = 0
        count = 0
        for i in range(len(nums)):
            s += nums[i]
            pre_sum.append(s)
        dic = {0:1}
        for i in range(1,len(pre_sum)):
            if dic.has_key(pre_sum[i] - k):
                    count += dic[pre_sum[i] - k]
            if dic.has_key(pre_sum[i]):
                dic[pre_sum[i]] += 1
            else:
                dic[pre_sum[i]] = 1

        return count
if __name__ == "__main__":


    A = [-1,-1,1]
    k = 0
    # A = [1, -1]
    # A = [-5,10,5,-3,1,1,1,-2,3,-4]
    s = Solution_leet()

    print s.subarraySum(A,k)