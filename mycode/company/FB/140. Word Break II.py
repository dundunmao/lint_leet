# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].

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

if __name__ == '__main__':
    s = Solution()
    x = "leetcode"
    y = ["leet", "code"]
    print s.wordBreak(x,y)