# -*- encoding: utf-8 -*-
# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 123,123,123,123  -> 123 Billion 123 Million 123 Thousand 123
# 2,123,123,123
class Solution(object):
    def __init__(self):
        """
        :type num: int
        :rtype: str
        """
        self.LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven","Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return 'Zero'
        i = 0
        words = ''
        while num > 0:
            if num % 1000 != 0:
                words = self.helper(num % 1000) + self.THOUSANDS[i] + " " + words   # 第一次 helper(789)+''+''；第二次helper(456)+''+'Thousand'+算好的789；第二次helper(123)+''+'Million'+算好的45689；
            num /= 1000
            i += 1
        return words.strip()
    def helper(self,num):
        if num == 0:
            return ''
        elif num < 20:
            return self.LESS_THAN_20[num] + ' '
        elif num < 100:
            return self.TENS[num/10] + ' ' + self.helper(num%10)
        else:
            return self.LESS_THAN_20[num / 100] + " Hundred " + self.helper(num % 100)