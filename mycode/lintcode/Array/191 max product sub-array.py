# -*- encoding: utf-8 -*-
# 找出一个序列中乘积最大的连续子序列（至少包含一个数）。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如, 序列 [2,3,-2,4] 中乘积最大的子序列为 [2,3] ，其乘积为6。
#DP,每轮记录一个min,一个max.从第一轮开始,就考虑nums[i]的正负,因此min就是负的,max就是正的.

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




class Solution_leet(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        res = nums[0]
        maxi = 1
        mini = 1
        for i in range(len(nums)):
            t = maxi
            print maxi * nums[i], mini * nums[i], nums[i]
            maxi = max(maxi * nums[i], mini * nums[i], nums[i])
            print maxi
            print "-----"
            print t * nums[i],  mini * nums[i], nums[i]
            mini = min(t * nums[i], mini * nums[i], nums[i])
            print mini
            print "-*--*--*"
            res = max(res, maxi)
        return res

if __name__ == "__main__":

    A = [2,2,3,-4,4,4,-3,2,-3]
    B = [-4,-3,-2]
    c = [2,3]
    s = Solution_leet()

    print s.maxProduct(A)