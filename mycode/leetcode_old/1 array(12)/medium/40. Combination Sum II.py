# -*- encoding: utf-8 -*-
# 4级
# 内容:给一个list和一个target,求list所有和等于target的组合,一个数只能用一次
# 思路: 递归.sort数组,遍历数组,轮到的这个数及其后面的数的组合=轮到的这个数的后面的部分sum为(target-这个数)的组合,然后每个组合都加上这个数



# recursive
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.search(candidates, 0 ,target)

    def search(self, candidates, start, target):
        if target==0:
            return [[]]
        res=[]
        for i in xrange(start,len(candidates)):
            if i!=start and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            for r in self.search(candidates, i+1, target-candidates[i]):
                res.append([candidates[i]]+r)       #[candidates[i]]为正轮到的这个element, r为组合的list.这里要把所有的list都加一个element
        return res

if __name__ == '__main__':
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print s.combinationSum2(candidates, target)