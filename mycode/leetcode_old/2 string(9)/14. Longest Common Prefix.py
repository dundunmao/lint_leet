# -*- encoding: utf-8 -*-
# 3级
# 题目：find the longest common prefix string amongst an array of strings.找出最长前缀
# 思路：用list里第一个str做标杆，取str里的第一个字符，看其他str里有没，然后再取第二个字符，看其他str里有没，直到没有，就return前面的字符
class Solution:
    # @param {string[]} strs
    # @return {string}

    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        str = strs[0]   #use first str to be the aim
        res = ''
        for i in range(len(str)):
            for j in range(1,len(strs)):
                if i > len(strs[j]) - 1: #if exceed the length
                    return res
                if str[i] != strs[j][i]: #if diff letter
                    return res
            res += str[i]
        return res

if __name__ == '__main__':
    s = Solution()