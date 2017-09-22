# -*- encoding: utf-8 -*-
# 求一串string里最长的无重复char的子串长度
# 基本同题406
class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        map = [0 for i in range(256)]
        i,j = 0,0
        ans = 0
        for i in range(len(s)):
            while j < len(s) and map[ord(s[j])] == 0:
                map[ord(s[j])] = 1
                ans = max(ans, j-i+1)
                j+=1
            map[ord(s[i])] = 0
        return ans


# two pointer，i等着起点，j往前走，边走边加入hash,
# 当发现hash里已经有了的时候，i要走到已经有的那个char的下一位，i边走边减hash里的ele
class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case
        if s == '':
            return 0
        #
        hash = {}
        res = 0
        i = 0
        j = i
        while i < len(s) and j < len(s):
                if not hash.has_key(s[j]):
                    hash[s[j]] = j
                    res = max(res, j-i+1)
                    j+=1
                else:
                    temp = hash[s[j]] + 1
                    while i < temp:
                        del hash[s[i]]
                        i += 1
                    hash[s[j]] = j
                    res = max(res, j-i+1)
                    j += 1
        return res
if __name__ == "__main__":
    s = Solution2()
    x = "abba"
    print s.lengthOfLongestSubstring(x)