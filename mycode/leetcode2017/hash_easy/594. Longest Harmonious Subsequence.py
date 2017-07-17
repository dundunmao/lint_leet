# -*- encoding: utf-8 -*-
# 给一个array找其中最大最小值相差正好为1的Subsequence
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 方法一，放入hash里，然后双循环查每一个对应其他的差是不是1
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ans = 0
        for ele in nums:
            if dic.has_key(ele):
                dic[ele] += 1
            else:
                dic[ele] = 1
        for k, v in dic.items():
            for key, val in dic.items():
                if k - key == 1:
                    ans = max(ans, v + val)
                    break
        return ans


class Solution_leet(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ans = 0
        for ele in nums:
            if dic.has_key(ele):
                dic[ele] += 1
            else:
                dic[ele] = 1
        for num in nums:
            if num + 1 in dic:
                ans = max(ans, dic[num] + dic[num + 1])
        return ans

