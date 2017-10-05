# -*- encoding: utf-8 -*-
# 一个原本的string：haystack和一个target string：needle。找haystack里有没有needle. needle里可能有*，他代表任一个字符
def strStr(self, haystack, needle):
    for i in range(len(haystack)):
        j = 0
        while i < len(haystack) and j < len(needle) and (needle[j] == '*' or haystack[i] == needle[j]):
            if j == len(needle)-1:
                return i
            i += 1
            j += 1
    return -1
