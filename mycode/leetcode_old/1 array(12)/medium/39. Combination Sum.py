# coding:utf-8
# 3级
# 题目 一个list C和一个target,找到所有的组合,使他们的合等于target,每个数能用很多遍
# 思路 跟18题像, 用recursive的方法


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        if not candidates or not target:
            return []
        result = []
        path = []
        self.DFS(candidates, path, target,result) # Use DFS to record results
        return result

    def DFS(self, candidates, path, target,result):
        if target < 0 :
            return
        elif target == 0:
            result.append(path)
        else:
            for i,x in enumerate(candidates):
                if x <= target: # target比x小,x加任何数都不可能等于target,这个组合就是0个数了
                    self.DFS(candidates[i:], path +[x], target-x,result) # canidates[i:]从i开始取,而18题是从i+1开始取,因为这里面一个数可以用无数遍,所以每次都是用其中一个数跟整个list组合,
            return
if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    print s.combinationSum(candidates, target)