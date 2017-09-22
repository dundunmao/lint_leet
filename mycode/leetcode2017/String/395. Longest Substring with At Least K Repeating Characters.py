# -*- encoding: utf-8 -*-


#找最长的substring，保证里面每个数都重复至少k次
# Example 1:
# Input: s = "aaabb", k = 3
# Output: 3。 The longest substring is "aaa", as 'a' is repeated 3 times.

# Example 2:
# Input:
# s = "ababbc", k = 2
# Output:5。The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

# 解法：先找到最小的频次的那个字母，如果他的频次大于K，那string里所有char都符合条件，return len(string)
#        否则以这个字母为分界点(因为result的substring一定不包括这个字母)，把string分开成n个substring。看substring里有没有符合的
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        array = []
        return self.helper(s, k, array)
    def helper(self, s, k, array):
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        le = 0
        for str in s.split('c'):
            le = max(le, self.longestSubstring(str,k))

        return le


if __name__ == "__main__":
    str = 'abcbbcaba'
    k = 3
    s = Solution()
    print s.longestSubstring(str,k)