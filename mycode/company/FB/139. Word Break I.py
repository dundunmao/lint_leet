# -*- encoding: utf-8 -*-
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".

# backtracking 超时
class Solution(object):
    def wordBreak(self, s, wordDict):
        # edge case
        if len(s) == 0 or s == '':
            return False
        pos = 0
        length = [len(ele) for ele in wordDict]
        return self.helper(s, wordDict,pos,length)

    def helper(self,s, wordDict, pos,length):
        # for i in range(pos,len(s)):
        if pos == len(s):
            return True
        for le in length:
            if s[pos:pos+le] in wordDict:
                if self.helper(s, wordDict, pos+le, length):
                    return True
        return False
# DP
class Solution1(object):
    def wordBreak(self, s, wordDict):
        f = [False for i in range(len(s))]
        f.insert(0,True)
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if f[j] == True and s[j:i] in wordDict:
                    f[i] = True
        return f[len(s)]

if __name__ == '__main__':
    s = Solution1()
    x = "leetcode"
    y = ["leet", "code"]
    print s.wordBreak(x,y)