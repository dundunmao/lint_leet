# -*- encoding: utf-8 -*-
# 3级
# 题目；DNA由A,C,G组成,给一串DNA,找出所有10个字母长的出现过不只一次的substrings.例如
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
#思路:从头到尾,十个字母为一个element,往dict里面放,找重复的.
def findRepeatedDnaSequences(self, s):
    dictionary = dict()
    for i in [s[x : x + 10] for x in range(len(s) - 9)]: #没十个字母为一个element,x为每个element的起点的index, s[x:x+10]为取出来的element,
        dictionary[i] = dictionary.get(i, 0) + 1  #如果这个key没有value,value就为0+1,如果有value,就为value+1
    return [k for k, v in dictionary.iteritems() if v > 1]  #如果value>1,取里面的value