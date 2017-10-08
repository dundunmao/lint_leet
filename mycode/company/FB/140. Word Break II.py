# -*- encoding: utf-8 -*-
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].
# 递归：超时
class Solution(object):
    def wordBreak(self, s, wordDict):
        # edge case
        if len(s) == 0 or s == '':
            return False
        pos = 0
        length = set([len(ele) for ele in wordDict])
        res = []
        temp = []
        self.helper(s, wordDict, pos, length, res, temp)
        return res

    def helper(self,s, wordDict, pos,length,res,temp):
        # for i in range(pos,len(s)):
        if pos == len(s):
            res.append(' '.join(temp[:]))
            return
        for le in length:
            if pos+le <= len(s) and s[pos:pos+le] in wordDict:
                temp.append(s[pos:pos+le])
                self.helper(s, wordDict, pos+le, length,res,temp)
                temp.pop()

class Solution_leet(object):
    def wordBreak(self, s, wordDict):
        # edge case
        if len(s) == 0 or s == '':
            return []
        start = 0
        hash = {}
        length = set([len(ele) for ele in wordDict])
        res = self.helper(s, wordDict, length, start, hash)
        return [' '.join(temp[:]) for temp in res]

    def helper(self, s, wordDict, length, start, hash):
        if hash.has_key(start):
            return hash[start]
        res = []
        for le in length:
            if start + le <= len(s) and s[start:start + le] in wordDict:
                list = self.helper(s, wordDict, length, start + le, hash)
                if not (list == [] and start != len(s)):
                    for ele in list:
                        res.append([s[start:start + le]] + ele)
                elif list == [] and start + le == len(s):
                    res.append([s[start:start + le]])
        hash[start] = res
        return res




if __name__ == '__main__':
    # s = Solution_leet()
    s = Solution_leet()
    # x = "catsanddog"
    # y = ["cat", "cats", "and", "sand", "dog"]
    x = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    y = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print s.wordBreak(x,y)