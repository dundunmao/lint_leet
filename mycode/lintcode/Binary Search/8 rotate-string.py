# -*- encoding: utf-8 -*-
# 给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 对于字符串 "abcdefg".
#
# offset=0 => "abcdefg"
# offset=1 => "gabcdef"
# offset=2 => "fgabcde"
# offset=3 => "efgabcd"

class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        if s is None or len(s) == 0 or offset is None:
            return None
        if offset == 0:
            return s
        offset = offset % len(s)   #去掉整轮的.
        while offset>0:
            s = s[-1]+s[:-1]
            offset-=1
        return s
if __name__ == "__main__":
    x = "abcdefg"
    offset = 3
    s = Solution()
    print s.rotateString(x,offset)