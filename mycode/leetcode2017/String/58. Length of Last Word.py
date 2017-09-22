# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
            else:
                break
        if i < 0:
            return 0
        count = 0
        print i
        for j in range(i, -1, -1):
            if s[j] != ' ':
                count += 1
            else:
                break
        return count
