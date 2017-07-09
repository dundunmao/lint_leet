# coding:utf-8
# 3级
# 题目:Given a set of distinct integers, nums, return all possible subsets.给一个无重复的list,出所以subset.


# DFS recursively
class Solution(object):
    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)

    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results


# Bit Manipulation
class Solution1(object):
    def subsets(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

# Iteratively
class Solution2(object):
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res
        # [[]]
        # [[],[1]]
        # [[],[1],[2],[1,2]]
        # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

if __name__ == '__main__':
    nums = [1,2,3]
    s= Solution2()
    print s.subsets(nums)