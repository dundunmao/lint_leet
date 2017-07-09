# -*- encoding: utf-8 -*-
# 题目:无重复的set, 求subsets
# 例如:input:[1,2,3]
#  output:
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


if __name__ == "__main__":
    nums = [1,2,3]
    s = Solution()

    print s.subsets(nums)