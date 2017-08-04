# coding:utf-8
# 在一个数组中找到前K大的数
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 [3,10,1000,-99,4,100], k = 3.
# 返回 [1000, 100, 10]
# http://www.jiuzhang.com/solutions/top-k-largest-numbers/
# 这个用内在函数不是考点
class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        nums.sort()
        l = len(nums)
        result = nums[-k:]
        result.reverse()
        return result
import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        topk.sort()
        topk.reverse()
        return topk







if __name__ == '__main__':
    nums = [1,2,3,4,5,6,8,9,10,7]
    k = 10
    s = Solution()
    print s.topk(nums, k)