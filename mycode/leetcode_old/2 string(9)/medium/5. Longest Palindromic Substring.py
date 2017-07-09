# -*- encoding: utf-8 -*-
# 3级
# 题目:给一个string,找到最长的palindromic substring,假设string长度不超过1000,只有一个最长的palindromic.
# 思路: 找到i+1和i-1所指一样的数,然后继续各自加减.记录长度
def longestPalindrome(s):
    lenS = len(s)
    if lenS <= 1: return s
    minStart = 0
    maxLen = 1
    i = 0
    while i < lenS:
        j, k = i, i
        while k < lenS - 1 and s[k] == s[k + 1]: #如果遇到两个一样的字母,j指前面那个,i和k指后面那个
            k += 1
        i = k + 1
        while k < lenS - 1 and j and s[k + 1] == s[j - 1]:#如果i的前面和后面的字母一样,j和k分别指向这两个
            k, j = k + 1, j - 1
        if k - j + 1 > maxLen:    #k和j的间隔+1.就是这一段的长度
            minStart, maxLen = j, k - j + 1 #更新起始点和长度
    return s[minStart: minStart + maxLen]
if __name__ == "__main__":
    s = 'abcdftytfdcbaab'
    print longestPalindrome(s)