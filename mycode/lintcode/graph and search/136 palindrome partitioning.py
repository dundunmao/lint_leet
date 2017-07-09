# -*- encoding: utf-8 -*-
# 给定一个字符串s，将s分割成一些子串，使每个子串都是回文串。
#
# 返回s所有可能的回文串分割方案。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 s = "aab"，返回
#
# [
#   ["aa", "b"],
#   ["a", "a", "b"]
# ]
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if s is None:
            return []
        result = []
        path = []
        # pos = 0
        self.help_function(s,path,0,result)
        return result

    def help_function(self,s, path,pos,result):
        if pos == len(s):   #起始点遍历到最后一位时,说明完成了.
            path_save = [x for x in path]
            result.append(path_save)
            return
        for i in range(pos,len(s)):
            prefix = s[pos:i+1]
            if not self.isPalindrome(prefix):
                continue
            path.append(prefix)
            self.help_function(s, path, i+1, result)
            path.pop()

    def isPalindrome(self, s):
        beg = 0
        end = len(s)-1
        while beg < end:
            if s[beg] != s[end]:
                return False
            beg += 1
            end -= 1
        return True

if __name__ == '__main__':
    s = "aab"
    x = Solution()
    print x.partition(s)
