# -*- encoding: utf-8 -*-
# 题目：Given 2*n + 1 numbers, every numbers occurs twice except one, find it.
# 方法：位运算
#     ^位运算,遇到相同的，就得0，遇到不同的就等1.
# 因此当两个相同数字遇到时，就全清零。相当于相同的数互消了。最后留下的就是那个当个的数
class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        ans = 0
        for x in A:
            ans = ans ^ x
        return ans