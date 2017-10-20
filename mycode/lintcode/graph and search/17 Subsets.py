# -*- encoding: utf-8 -*-
# 给定一个含不同整数的集合，返回其所有的子集
#
#  注意事项
#
# 子集中的元素排列必须是非降序的，解集必须不包含重复的子集
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 如果 S = [1,2,3]，有如下的解：
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        res = [[]]
        path = []
        self.helper(nums, res, path)
        return res
    def helper(self, nums, res, path):
        for i in range(len(nums)):
            path.append(nums[i])
            res.append(path[:])
            self.helper(nums[i+1:], res, path)
            path.pop()

class Solution1:

    def sum_subarray(self, arr):
        res = []
        array = []
        pos = 0
        self.helper(arr, res, array, pos)
        ans = 0
        for ele in res:
            ans += sum(ele)
        return ans

    def helper(self, arr, res, array, pos):
        for i in range(pos, len(arr)):
            array.append(arr[i])
            res.append(array[:])
            self.helper(arr, res, array, i + 1)
            array.pop()

class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in sorted(nums):
            result += [item + [num] for item in result]
        return result


if __name__ == '__main__':
    S = [1,2,3]
    s = Solution1()
    print s.sum_subarray(S)