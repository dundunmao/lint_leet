# coding:utf-8
# 给出字符串S和字符串T，计算S的不同的子序列中T出现的个数。
#
# 子序列字符串是原始字符串通过删除一些(或零个)产生的一个新的字符串，并且对剩下的字符的相对位置没有影响。(比如，“ACE”是“ABCDE”的子序列字符串,而“AEC”不是)。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出S = "rabbbit", T = "rabbit"
#
# 返回 3
class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
        func = [[0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]
        for i in range(len(S) + 1):
   			func[i][0] = 1
        for i in xrange(1, len(S)+1):
            for j in xrange(1, len(T)+1):
                if S[i-1] == T[j-1]:
                    func[i][j] = func[i-1][j] + func[i-1][j-1]
                else:
                    func[i][j] = func[i-1][j]
        return func[len(S)][len(T)]