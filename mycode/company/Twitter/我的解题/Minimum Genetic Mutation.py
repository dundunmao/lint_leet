# -*- encoding: utf-8 -*-
# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
#
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
#
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
#
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
#
# Note:
#
# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.
# Example 1:
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# return: 1
# Example 2:
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# return: 2
# Example 3:
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# return: 3

# 方法：典型BFS

from collections import deque


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # edge case
        if end not in bank or bank == [] or start is None:
            return -1

        # main part
        count = -1
        q = deque()
        q.append(start)
        hash = {}
        while q:
            le = len(q)
            count += 1
            for i in range(le):
                print q
                po = q.popleft()
                if po == end:
                    return count
                for j in range(len(po)):
                    for ele in ['A', 'C', 'G', 'T']:
                        new = po[:j] + ele + po[j + 1:]
                        if new in bank:
                            if new not in hash:
                                q.append(new)
                                hash[new] = True
        return -1

if __name__ == "__main__":
    a = "AACCTTGG"
    b = "AATTCCGG"
    c = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]

    s = Solution()
    print s.minMutation(a,b,c)