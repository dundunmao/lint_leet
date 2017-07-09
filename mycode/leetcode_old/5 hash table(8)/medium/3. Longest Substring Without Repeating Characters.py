# -*- encoding: utf-8 -*-
# 3.5级
# 题目:给一个string,找到最长的substring让里面没有重复的字母,例如"abcabcbb"->"abc", "bbbbb"->"b"
# 思路:往dict里面加元素对,key为字母,value为最新的没有重复的index,
def lengthOfLongestSubstring(s):
    start = maxLength = 0
    usedChar = {}
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]: #如果有重复的,并且,start不能在被重复的那个数的后面(如果start在被重复的数的后面,那个被重复的数就无关紧要了,反正也不会算进去,所以start就不用重新计算,)
            start = usedChar[s[i]] + 1              #如果有重复的,start要从重复的下一个开始记,所以要+1
        else:
            maxLength = max(maxLength, i - start + 1)  #算从遍历到的那个点到start的差,要+1因为算的是一共有多少字母
        usedChar[s[i]] = i
    return maxLength


if __name__ == "__main__":
    s = "abcabcde"
    s = "bbbbb"
    s = "ab"
    print lengthOfLongestSubstring(s)