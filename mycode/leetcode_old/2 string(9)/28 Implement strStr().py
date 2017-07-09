# -*- encoding: utf-8 -*-
#2.5级
# 题目：对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。
# 如果不存在，则返回 -1。haystack是source,needle是target
# 思路：双层循环，外层遍历大string,里层遍历小string,如果发现第一个相同，i,j同时向后走
class Solution:
    def strStr(self, source, target):
        # corner case:
        if source is None or target is None:
            return -1
        if source == '' and target == '':
            return 0
        if source == '' and target != '':
            return -1
        if target == '' and source != '':
            return 0
        # main part
        for i in range(len(source)):
            j = 0
            k = i
            while j < range(len(target)):
                if source[k] == target[j]:
                    k += 1
                    j += 1
                else:
                    break
                if j == len(target):
                    return i
        return -1

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if haystack == None or needle == None or len(haystack) < len(needle):
        return -1
    if haystack == needle or needle == "":
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        flag = True
        res = i
        for char in needle:
            if char == haystack[i]:      #一旦找到了相同的
                i += 1                   #i+=1就是haystack也同时往下走
            else:
                flag = False             #一旦发现不同,就break
                break
        if flag:                         #一旦needle遍历完了flag还是true,那就返回res
            return res
    return -1

if __name__=='__main__':
    haystack = '123456'
    needle = '34'
    print strStr(haystack, needle)









