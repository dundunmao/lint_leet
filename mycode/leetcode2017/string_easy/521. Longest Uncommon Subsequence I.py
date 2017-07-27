# -*- encoding: utf-8 -*-
# 最长不同subsequence
# 给两个string，找到最长的uncommon subsequence，意思是两个subsequent来自两个string，他们不一样。
# Input: "aba", "cdc"
# Output: 3
# Explanation: The longest uncommon subsequence is "aba" (or "cdc"),
# because "aba" is a subsequence of "aba",
# but not a subsequence of any other strings in the group of two strings.
class Solution(object):
    def findLUSlength(self, A, B):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if A == B:
            return -1
        return max(len(A), len(B))