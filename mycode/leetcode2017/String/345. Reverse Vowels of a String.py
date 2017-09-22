# -*- encoding: utf-8 -*-
# 给一个string，把里面的vowels reverse了
# Example 1:
# Given s = "hello", return "holle".
# Example 2:
# Given s = "leetcode", return "leotcede".
# Note:
# The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = ['a','e','o','u','i','A','E','O','U','I']
        i= 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            while s[i] not in array:
                i += 1
            while s[j]  not in array:
                j -= 1
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return ''.join(s)
#超时
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        array = ['a','e','o','u','i','A','E','O','U','I']
        index = []
        record = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in array:
                index.append(i)
                record.append(s[i])
        record.reverse()
        for j in range(len(s)):
            if j in index:
                s[j]=record[0]
                del record[0]
        return ''.join(s)

if __name__ == "__main__":
    a = "OE"
    x = Solution()
    print x.reverseVowels(a)
