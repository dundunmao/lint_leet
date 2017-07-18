# -*- encoding: utf-8 -*-
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        判断是否都是大写或都是小写或首字母大写
        """
        return word.isupper() or word.islower() or word.istitle()