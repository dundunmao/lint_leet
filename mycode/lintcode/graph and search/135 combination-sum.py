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

# class Solution1:
#     # @param candidates, a list of integers
#     # @param target, integer
#     # @return a list of lists of integers
#     def combinationSum(self, candidates, target):
#         # write your code here
#         candidates.sort()
#         Solution.ret = []
#         self.DFS(candidates, target, 0, [])
#         return Solution.ret
#
#     def DFS(self, candidates, target, start, path):
#         length = len(candidates)
#         if target == 0:
#             return Solution.ret.append(path)
#         for i in range(start, length):
#             if target < candidates[i]:
#                 return
#             self.DFS(candidates, target - candidates[i], i, path + [candidates[i]])

if __name__ == '__main__':
    candidates = [2,6,7]
    candidates2 =  [8, 7, 4, 3]
    target = 6
    target2 = 11
    s = Solution()
    print s.combinationSum(candidates2, target2)


