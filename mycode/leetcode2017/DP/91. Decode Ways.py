# -*- encoding: utf-8 -*-
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.

# 方法一 backtracking + memorization

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        if s == '0':
            return 0
        hash = {}
        return self.helper(s, 0, hash)

    def helper(self, s, pos, hash): #从pos为起点走，他就是把pos+1为起点和把pos+2为起点加起来
        if pos == len(s):
            return 1
        elif pos == len(s) + 1:
            return 0
        if hash.has_key(s[pos:]):   #先看hash里有没有
            return hash[s[pos:]]
        first = 0
        second = 0
        # 每往下走一步都有两种走法，走一格或走两格，走的时候要check可不可以走，我们需要把这两种方式加起来，
        if int(s[pos:pos + 1]) > 0: #如果这步大于0，可以走。否则走不通，不算了
            first = self.helper(s, pos + 1, hash) #可以走一格时，目前位置(i)的走法=下一个位置(i+1)的走法

        if int(s[pos:pos + 2]) <= 26 and int(s[pos:pos + 2]) > 9:  #如果这步在9-26之间，可以走。否则走不通，不算了
            second = self.helper(s, pos + 2, hash)

        hash[s[pos:]] = first + second  # hash记录
        return first + second

# DP
class Solution1(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        n = len(s)
        f = [0 for i in range(len(s) + 1)]
        f[0] = 1
        if s[0] == '0':
            f[1] = 0
        else:
            f[1] = 1
        for i in range(2,n+1):
            first = int(s[i-1:i])  #前一个
            second = int(s[i-2:i])  #前俩个
            if first >= 1 and first <= 9:
                f[i] = f[i-1]
            if second >= 10 and second <= 26:
                f[i] += f[i-2]
        return f[n]


if __name__ == "__main__":
    strs = "0"
    s = Solution1()
    print s.numDecodings(strs)