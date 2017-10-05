# -*- encoding: utf-8 -*-
# 找出一个序列中乘积最大的连续子序列（至少包含一个数）。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如, 序列 [2,3,-2,4] 中乘积最大的子序列为 [2,3] ，其乘积为6。
# DP,每轮记录一个min,一个max.从第一轮开始,就考虑nums[i]的正负,因此min就是负的,max就是正的.

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        # edge case
        if nums is None:
            return None
        if len(nums) == 0:
            return 0
        maxi = [nums[0]]
        mini = [nums[0]]
        result = nums[0]
        for i in range(1, len(nums)):
            mini.append(nums[i])
            maxi.append(nums[i])
            if nums[i] > 0:
                maxi[i] = max(maxi[i], maxi[i - 1] * nums[i])
                mini[i] = min(mini[i], mini[i - 1] * nums[i])
            elif nums[i] < 0:
                maxi[i] = max(maxi[i], mini[i - 1] * nums[i])
                mini[i] = min(mini[i], maxi[i - 1] * nums[i])
            result = max(result, maxi[i])
        return result


# 每次求包括当前数的max， min。max和min取得是当前数与前一次的max和min的乘积，以及当前数本身的最大和最小。
# 因为包括当前数的max:可能是从头一直乘过来的数（一直在正数块内），
#                   也可能是从负的乘过来的数（翻转了，如-3那，是积累了两个负的，所以这里的正数块就延伸成了粉色块），
#                   也可能是自己本身（如-4，4，因为前面遇到一个负的）。

class Solution_leet(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        maxi, mini= 1,1
        res = max(nums)
        record = [res]
        for i in range(len(nums)):
            maxi_last = maxi
            # 到i为止，包括当前nums[i]的最大乘积
            maxi = max(maxi_last * nums[i], mini * nums[i], nums[i])
            # 到i为止，包括当前nums[i]的最小乘积
            mini = min(maxi_last * nums[i], mini * nums[i], nums[i])
            res = max(res, maxi)
            record.append(res)
        return res


if __name__ == "__main__":





    A = [2,3,-4,4,4,-3,-2,-3,3,-3]
    B = [2,-5,-2,-4,3]
    c = [2,3]
    d = [-2,5,-4,6,0,6,40]
    s = Solution()

    print s.maxProduct(A)