# -*- encoding: utf-8 -*-
# 题：给一个string，问该string是不是起substring重复多次构成的
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(n/2,0,-1):
            if n % i == 0:
                c = n/i
                t = ''
                for j in range(0,c):
                    t = t + s[0:i]
                if t == s:
                    return True
        return False
if __name__ == "__main__":
    a = "ababab"
    x = Solution()
    print x.repeatedSubstringPattern(a)

