# -*- encoding: utf-8 -*-
# 3级
# 题目:'A' -> 1; 'B' -> 2...'Z' -> 26;给一个digit,返回the total number of ways to decode it.
# 例如 给 "12", it could be decoded as "AB" (1 2) or "L" (12).The number of ways decoding "12" is 2.
#
def numDecodings1(s):
    if s == "": return 0
    dp = [0 for x in range(len(s)+1)]
    dp[0] = 1
    for i in range(1, len(s)+1):
        if s[i-1] != "0":  #如果单个的数不为0,dp在这个位置的值为他前面位置的值
            dp[i] += dp[i-1]
        if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #如果两个连着的数在09-27之间,dp在这个位置的值等于他前面隔一个位置的值
            dp[i] += dp[i-2]
    return dp[len(s)]
if __name__ == "__main__":
    s = '1291'
    print numDecodings1(s)