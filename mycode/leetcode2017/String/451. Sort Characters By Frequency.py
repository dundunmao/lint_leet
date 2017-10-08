# -*- encoding: utf-8 -*-
# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash = Counter(s)
        # hash = {'e':2,'d':1}
        temp = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        res = []
        for k, v in temp:
            for i in range(v):
                res.append(k)
        return ''.join(res)

if __name__ == "__main__":
    a = "tree"
    b = "AATTCCGG"
    c = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]

    s = Solution()
    print s.frequencySort(a)