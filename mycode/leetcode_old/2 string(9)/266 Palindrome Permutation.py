# -*- encoding: utf-8 -*-
# 2级
# 题目：排列组合里有回文没.Given a string, determine if a permutation of the string could form a palindrome.
# 例如: "code" -> False, "aab" -> True, "carerac" -> True.
#
import collections
def canPermutePalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    dictCount = collections.Counter(s)
    listCount = dictCount.values()
    sum = 0
    for count in listCount:
        sum+=count%2
    return sum<2
    # return sum(v % 2 for v in collections.Counter(s).values()) < 2

if __name__ == "__main__":
    s = "carerac"
    print canPermutePalindrome(s)