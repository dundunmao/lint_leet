# -*- encoding: utf-8 -*-
# 3级 背下来
# 题目:给两词:word1 and word2, 找convert word1 to word2的最小步骤. (each operation is counted as 1 step.)
# You have the following 3 operations permitted on a word:
# a) Insert a character
# b) Delete a character
# c) Replace a character
# 解题:DP
# 对应位对比,不一样的就算一个step.
# 先设计如下矩阵
# [[0, 1, 2, 3, 4, 5],
#  [1, 0, 0, 0, 0, 0],
#  [2, 0, 0, 0, 0, 0],
#  [3, 0, 0, 0, 0, 0]]
# 然后如果对应位一样,这个地方就等于他的左上角; 否则,就等于左上,上,左,里面最小的那个+1
# 最后取右下角那个数的值
def minDistance(word1, word2):
#     """
#     :type word1: str
#     :type word2: str
#     :rtype: int
#     """
    if len(word1) > len(word2):
        word1,word2 = word2,word1
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
    m = len(word1)
    n = len(word2)
    d = [[0 for i in xrange(n+1)] for j in xrange(m+1)]
    for i in xrange(m+1):
        d[i][0] = i
    for i in xrange(n+1):
        d[0][i] = i
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if word1[i-1] == word2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i-1][j], d[i-1][j-1], d[i][j-1])
    return d[m][n]

if __name__ == "__main__":

    minDistance('ab', 'bc')
