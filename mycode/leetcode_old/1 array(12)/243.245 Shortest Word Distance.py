# coding:utf-8
# 题目:给list of words,找其中两个Word间的最短距离.(245题多一个条件是要考虑word1=word2 )
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Given word1 = “coding”, word2 = “practice”, return 3.
# Given word1 = "makes", word2 = "coding", return 1.
def shortestDistance(list, word1, word2):
    result2 = len(list)
    a = _indexList(list,word1)   #先得到两个单词的list of index
    b = _indexList(list,word2)
    i = 1
    while i<len(a):
        if a == b:  #如果word1=word2
            result1 = abs(a[i]-a[i-1])
            if result2 >result1:
                result2 = result1
        else:
            for j in range(len(b)):        #两个Word的index互相比,记下最小的那个
                result1 = abs(a[i]-b[j])
                if result2 >result1:
                    result2 = result1
        i+=1
    return result2
def _indexList(list,word):
    result = []
    for k in range(len(list)):
        if word == list[k]:
            result.append(k)
    return result
if __name__ == '__main__':
    list = ["practice", "makes", "practice","perfect","coding", "makes","practice"]
    word1 = 'practice'
    word2 = 'makes'
    print shortestDistance(list, word1, word2)