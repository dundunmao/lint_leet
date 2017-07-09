# coding:utf-8
# 实现一个算法确定字符串中的字符是否均唯一出现
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出"abc"，返回 true
#
# 给出"aab"，返回 false


class Solution:
    def isUnique(self, str):
        if len(str)<2:
            return True
        array = [False]*256
        for s in str:
            if array[ord(s)] == True:
                return False
            else:
                array[ord(s)] = True
        return True

    def isUnique_self(self, str):
        # write your code here
        if len(str)<2:
            return True
        hash = {}
        for s in str:
            if hash.has_key(s):
                return False
            else:
                hash[s] = True
        return True