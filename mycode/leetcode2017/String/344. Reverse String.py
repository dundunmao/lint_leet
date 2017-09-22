# -*- encoding: utf-8 -*-
# 学习reverse的build in 方法
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return s
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        s = ''.join(s)
        return s
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_temp=list(s)
        s_temp.reverse()
        return ''.join(s_temp)
if __name__ == "__main__":
    s = 'hello'
    x = Solution()
    print x.reverseString(s)