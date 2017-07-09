# coding:utf-8

# 给出两个单词word1和word2，计算出将word1 转换为word2的最少操作次数。
#
# 你总共三种操作方法：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 work1="mart" 和 work2="karma"
#
# 返回 3
class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        len1 = len(word1)
        len2 = len(word2)
        f = [[0] * (len2 + 1) for i in range(len1 + 1)]
        for i in range(len1 + 1):
            f[i][0] = i
        for j in range(len2 + 1):
            f[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word2[j - 1] == word1[i - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1

        return f[len1][len2]