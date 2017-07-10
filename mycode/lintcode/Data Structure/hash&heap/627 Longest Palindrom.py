class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    def longestPalindrome(self, s):
        # Write your code here
        dic = {}
        for str in s:
            if dic.has_key(str):
                dic[str] += 1
            else:
                dic[str] = 1
        result = 0
        single = 0
        for v in dic.values():
            if v % 2 == 0:
                result += v
            else:
                single = 1
                result += (v-1)
        if single:
            return result + 1
        else:
            return result