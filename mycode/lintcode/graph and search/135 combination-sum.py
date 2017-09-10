# -*- encoding: utf-8 -*-
# 给出一组候选数字(C)和目标数字(T),找到C中所有的组合，使找出的数字和为T。C中的数字可以无限制重复被选取。
#
# 例如,给出候选数组[2,3,6,7]和目标数字7，所求的解为：
#
# [7]，
#
# [2,2,3]
#
#  注意事项
#
# 所有的数字(包括目标数字)均为正整数。
# 元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
# 解集不能包含重复的组合。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出候选数组[2,3,6,7]和目标数字7
#
# 返回 [[7],[2,2,3]]
class Solution:
    def combinationSum(self, candidates, target):
        if candidates is None:
            return []
        result = []
        path = []
        candidates.sort()
        self.helper_function(candidates, target, path, 0, result)
        return result

    def helper_function(self,candidates, target, path, index, result):
        # result = []
        if target == 0:
            path_save = [x for x in path]
            result.append(path_save)
        prev = -1
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            if prev != -1 and prev == candidates[i]:
                continue
            path.append(candidates[i])
            self.helper_function(candidates, target - candidates[i], path, i, result)
            path.pop()

            prev = candidates[i]

class Solution1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        pos = 0
        candidates.sort()
        self.helper(candidates, target, path, res, pos)
        return res
    def helper(self, A, target, path, res, pos):
        if target == 0:
            res.append(path[:])
            return
        for i in range(pos, len(A)):
            if A[i] > target:
                break
            path.append(A[i])
            self.helper(A, target - A[i], path, res, i)
            path.pop()

if __name__ == '__main__':
    candidates = [2,6,7] #[[7],[2, 2, 3]]
    candidates2 =  [8, 7, 4, 3]  #[[3, 4, 4], [3, 8], [4, 7]]
    target = 7
    target2 = 11
    s = Solution1()
    print s.combinationSum(candidates2, target2)


