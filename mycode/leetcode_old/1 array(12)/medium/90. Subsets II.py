# coding:utf-8
# 3级
# 题目:Given a set of distinct integers, nums, return all possible subsets.给一个有重复的list,出所以subset.

class Solution2(object):
    def _subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        # result = [ele for ele in res if ele not in result]
        res = [res[i] for i in range(len(res)) if res[i] not in res[:i]]
        return res
        # [[]]
        # [[],[1]]
        # [[],[1],[2],[1,2]]
        # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

if __name__ == '__main__':
    nums = [1,2,2]
    s= Solution2()
    print s._subsets(nums)