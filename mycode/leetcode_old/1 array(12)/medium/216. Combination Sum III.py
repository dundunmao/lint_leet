# -*- encoding: utf-8 -*-
# 4级
# 内容:从1-9中取k个数,使其和等于n.例如:k = 3, n = 9 输出:[[1,2,6], [1,3,5], [2,3,4]]
#思路.

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if n > sum([i for i in range(1, 11)]): #如果1到10加起来还没有n大,那就不可能有组合成立了
            return []
        res = []
        self.sum_help(k, n, 1, [], res)
        return res
    def sum_help(self, k, n, curr, arr, res):
        if len(arr) == k:
            if sum(arr) == n:
                res.append(list(arr))
            return
        if len(arr) > k or curr > 9:
            return
        for i in range(curr, 10):
            arr.append(i)
            self.sum_help(k, n, i + 1, arr, res)
            arr.pop()
if __name__ == '__main__':
    k = 3
    n = 9
    s = Solution()
    print s.combinationSum3(k, n)