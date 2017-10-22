# -*- encoding: utf-8 -*-
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # array = s.strip().split()[::-1]
        # if s == '' or s == ' ':
        #     return ''
        s = s.strip()  # 去掉前后的空格
        if s == '':
            return ''
        array = s.split()  # 用空格把它分成array
        array.reverse()
        return ' '.join(array)
if __name__ == "__main__":
    s = "the sky is blue"
    x = Solution()
    print x.reverseWords(s)