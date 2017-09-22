# -*- encoding: utf-8 -*-
# 问string里有多少个连续无空格的substring
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        count = 0

        pre = s[0]
        for i in range(1,len(s)):
            if s[i] == ' ' and s[i] != pre:
                count += 1
            pre = s[i]
        return count + 1

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
if __name__ == "__main__":
    a = "Hello, my name is John "
    x = Solution()
    print x.countSegments(a)