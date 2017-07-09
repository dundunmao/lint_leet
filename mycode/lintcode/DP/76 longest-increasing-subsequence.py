# -*- encoding: utf-8 -*-
# 给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# 最长上升子序列的定义：
#
# 最长上升子序列问题是在一个无序的给定序列中找到一个尽可能长的由低到高排列的子序列，这种子序列不一定是连续的或者唯一的。
# https://en.wikipedia.org/wiki/Longest_increasing_subsequence
#
# 样例
# 给出 [5,4,1,2,3]，LIS 是 [1,2,3]，返回 3
# 给出 [4,2,4,5,3,7]，LIS 是 [2,4,5,7]，返回 4
# DP
class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None:
            return 0
        f = [1 for i in range(len(nums))]
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i] and f[i]<=f[j]+1:
                        f[i] = f[j]+1
        return max([ele for ele in f])

# binary search O(nlogn)
class Solution1:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        minLast = [float('inf') for i in range(len(nums)+1)]
        minLast[0] = -1
        for i in range(len(nums)):
            index = self.binarySearch(minLast,nums[i])
            minLast[index] = nums[i]
        for i in range(len(nums), -2,-1):
            if minLast[i] != float('inf'):
                return i
        return 0
    def binarySearch(self, minLast, num):
        start = 0
        end = len(minLast)-1
        while start+1<end:
            mid = start+(end-start)/2
            if minLast[mid] < num:
                start = mid
            else:
                end = mid
        if minLast[start]>num:
            return start
        return end

# 我的练习: DP法:
# f = [1,1,1,1]
# f[i] = 他前面的nums里第一个 nums[j]<nums[i],这时候的j就是腰找的f[j]
# f[i] = f[j]+1

class Solution2:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
        le = len(nums)
        f = [1 for i in range(le)]
        for i in range(1, le):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    new = f[j] + 1
                    f[i] = max(f[i], new)
        return max(f)
# 老公的方法: recursive
def obtain_length_LISubSuq(ori_s):
   nn = 0
   nss = []

   if len(ori_s) == 0:
       return 0, [[]]
   elif len(ori_s) == 1:
       return 1, [ori_s]

   n, ss = obtain_length_LISubSuq(ori_s[:len(ori_s) - 1])
   for s in ss:
       ns =[]
       if ori_s[-1] > s[-1]:
           nss.append(s)
           ns = s + [ori_s[-1]]
           nss.append(ns)
       else:
           ns = s
           nss.append(ns)
       if nn < len(ns):
           nn = len(ns)

   nss.append([ori_s[-1]])
   return nn, nss


if __name__ == "__main__":
    nums = [10,1,11,2,12,3,11]
    print obtain_length_LISubSuq(nums)
    s = Solution()
    print s.longestIncreasingSubsequence(nums)