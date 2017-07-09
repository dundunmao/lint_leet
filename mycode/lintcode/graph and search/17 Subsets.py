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
class Solution:

    def subsets(self, S):
        result = []
        if S is None or len(S) == 0:
            return []
        list = []
        S.sort()
        result_1 = []
        result = []
        self.helper(result, list, S, 0,result_1)
        res = result_1+[[]]
        return result,res,result.sort() == res.sort()
#以pos开头的S里的数的subsets
    def helper(self, result, list, S, pos,result_1):
        list_get = [x for x in list]
        result.append(list_get)
        for i in range(pos, len(S)):
            list.append(S[i])
            list_g = [x for x in list]
            result_1.append(list_g)   #可以放在这里append
            self.helper(result, list, S, i + 1,result_1)
            list.pop()

class Solution1(object):
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
    S = [1,2,3,4]
    s = Solution()
    print s.subsets(S)