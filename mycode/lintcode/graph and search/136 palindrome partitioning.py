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

# traverse
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if s is None:
            return []
        result = []
        path = []
        pos = 0
        self.help_function(s,path,pos,result)
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

# divide&conquer
class Solution1(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s == '':
            return False
        return self.helper(s)
    def helper(self, s):
        if s == '':
            return []
        if len(s) == 1:
            return [[s]]
        res = []
        for i in range(1, len(s) + 1):
            if self.is_pali(s[:i]):
                A = self.helper(s[i:])
                if A == []:
                    res.append([s[:i]])
                for ele in A:
                    res.append([s[:i]] + ele)
        return res
    def is_pali(self, s):  # return boolean
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = "aab"
    s = 'cbb'
    x = Solution1()
    print x.partition(s)
