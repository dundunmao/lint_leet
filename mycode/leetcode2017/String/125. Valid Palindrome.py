# -*- encoding: utf-8 -*-
# 给string，问是不是palindrome，considering only alphanumeric characters and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 要考虑大小写，考虑是不是字母和数字（isalnum）
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        array = []
        for str in s:
            if str.isalnum():
                array.append(str.lower())
        return self.pa(array)

    def pa(self, array):
        i = 0
        j = len(array) - 1
        while i < j:
            if array[i] != array[j]:
                return False
            i += 1
            j -= 1
        return True
