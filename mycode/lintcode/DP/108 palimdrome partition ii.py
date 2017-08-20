# coding:utf-8

# 给定一个字符串s，将s分割成一些子串，使每个子串都是回文。
#
# 返回s符合要求的的最少分割次数。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如，给出字符串s = "aab"，
#
# 返回 1， 因为进行一次分割可以将字符串s分割成["aa","b"]这样两个回文子串
# 记忆化搜索的DP
class Solution:
    def palimdrome(self, s):
        is_pa= [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            is_pa[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                is_pa[i][i+1] = True
            else:
                is_pa[i][i + 1] =False
        for i in range(len(s)-1,-1,-1):
            for j in range(i+2,len(s)):
                is_pa[i][j] = is_pa[i+1][j-1] and (s[i] == s[j])
        return is_pa
    def minCut(self, s):
        if s is None or len(s) == 0:
            return 0
        is_pa = self.palimdrome(s)
        func = [i for i in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if is_pa[j][i - 1]:
                    func[i] = min(func[i], func[j] + 1)
        return func[len(s)] - 1

#这种是正在DP，但是超时，所以要把palindrome存矩阵里
class Solution1(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case
        if s is None or len(s) == 0:
            return 0
        # normal case
        f = [i for i in range(len(s))]
        f.insert(0, -1)
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if self.is_p(s[j:i]):
                    f[i] = min(f[i], f[j] + 1)
        return f[len(s)]

    def is_p(self, s):  # return boolean
        if len(s) == 0:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
if __name__ == "__main__":
    s = 'aab'
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    x = Solution1()
    print x.minCut(s)


