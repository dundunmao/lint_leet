# -*- encoding: utf-8 -*-
# 给定一个可能具有重复数字的列表，返回其所有可能的子集
#
#  注意事项
#
# 子集中的每个元素都是非降序的
# 两个子集间的顺序是无关紧要的
# 解集中不能包含重复子集
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 如果 S = [1,2,2]，一个可能的答案为：
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
class Solution:

    def permutation(self, S):
        result = []
        if S is None or len(S) == 0:
            return []
        list = []
        S.sort()
        self.helper(result, list, S, 0)
        return result

    def helper(self, result, list, S, pos):
        repeat = None

        for i in range(pos, len(S)):
            if S[i] == repeat:
                continue
            else:
                list.append(S[i])

            list_get = [x for x in list]
            result.append(list_get)

            self.helper(result, list, S, i + 1)
            repeat = list.pop()

class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        path = []
        nums.sort()
        self.helper(nums, res, path)
        return res
    def helper(self, nums, res, path):
        for i in range(len(nums)):
            path.append(nums[i])
            if path not in res:
                res.append(path[:])
                self.helper(nums[i+1:], res, path)
            path.pop()
if __name__ == '__main__':
    S = [1,2,2]
    s = Solution()
    print s.permutation(S)