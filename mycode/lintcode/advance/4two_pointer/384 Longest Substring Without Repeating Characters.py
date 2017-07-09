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


# follow up:求一串string里最长子串,其中不能有char重复k次以上
def lengthOfLongestSubstringKDistinct(s, k):
    # write your code here
    # max_len = 0
    map = [0 for i in range(256)]
    i, j = 0, 0
    ans = 0
    for i in range(len(s)):
        while j < len(s):
            map[ord(s[j])] += 1
            if map[ord(s[j])] == k + 1:
                ans = max(ans, j - i)
                break
            j += 1
        map[ord(s[i])] -= 1
    return ans
if __name__ == "__main__":
    s = Solution()
    x = "abcabcbb"
    print s.lengthOfLongestSubstring(x)