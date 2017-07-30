# -*- encoding: utf-8 -*-
# Example
# Given s = "cbaebabacd" p = "abc"
# return [0, 6]
#
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

class Solution:
    # @param {string} s a string
    # @param {string} p a non-empty string
    # @return {int[]} a list of index
    def findAnagrams(self, s, p):
        # Write your code here
        if len(s) < len(p):
            return []
        dic = {}
        result = []
        for str in p:
            if str not in dic:
                dic[str] = 1
            else:
                dic[str] += 1
        count = len(dic)
        le = float('inf')
        i = 0
        j = 0
        while j < len(s):
            if dic.has_key(s[j]):
                dic[s[j]] -= 1
                if dic[s[j]] == 0: #value为0了，count才减，所以count为0时，说明这一段就是anagrams
                    count -= 1
            j += 1
            while count == 0:
                if j - i == len(p): #Windows
                    result.append(i)
                if dic.has_key(s[i]):
                    dic[s[i]] += 1
                    if dic[s[i]] >0:
                        count += 1
                i += 1
        return result

if __name__ == '__main__':
    a = "cbaebabacd"
    b = "abc"
    s = Solution()
    print s.findAnagrams(a,b)