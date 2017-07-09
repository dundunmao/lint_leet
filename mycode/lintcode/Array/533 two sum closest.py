# -*- encoding: utf-8 -*-
# 找到两个数字使得他们和最接近target
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# nums = [-1, 2, 1, -4],target = 4.
#
# 最接近值为 1
class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumCloset(self, nums, target):
        # Write your code here
        nums.sort()
        k = 0
        j = len(nums)-1
        mini = float('inf')
        while k<j:
            mini = min(mini,abs(target-nums[k]-nums[j]))
            if target-nums[k]-nums[j] > 0:
                i += 1
                continue
            elif target-nums[k]-nums[j] < 0:
                j -= 1
                continue
            elif target-nums[k]-nums[j] == 0:
                return 0
        return mini

# 我的brutal force
class Solution1:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumCloset(self, nums, target):
        # Write your code here
        nums.sort()
        diff = float('inf')
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if diff > abs(target - nums[i] - nums[j]):
                    diff = abs(target - nums[i] - nums[j])
                    result = diff
        return result
class Solution2:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumCloset(self, nums, target):
        # Write your code here
        nums.sort()
        diff = float('inf')
        k = 0
        j = len(nums)-1
        while k<j:
            x = target - (nums[k] + nums[j])
            diff = min(diff,abs(x)) #注意要求这个mini因为很可能打印出来如下
            print x   #-8483，-2119，-96，204，191，136
            if x < 0:
                j-=1
            elif x > 0:
                k +=1
            else:
                return 0
        return diff
if __name__ == "__main__":


    A = [1,2,33,23,2423,33,23,1,7,6,8787,5,33,2,3,-23,-54,-67,100,400]
    B = 237

    s = Solution2()

    print s.twoSumCloset(A,B)