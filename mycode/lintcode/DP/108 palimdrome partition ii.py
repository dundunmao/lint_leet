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
class Solution:
    # @param s, a string
    # @return an integer
    # def palimdrome(self, s):
    #     i = 0
    #     while i <= len(s) - 1:
    #         if s[i] != s[-i - 1]:
    #             return False
    #         else:
    #             i += 1
    #     return True
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
    def palimdrome1(self, s):
        is_pa= [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            is_pa[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                is_pa[i][i+1] = True
            else:
                is_pa[i][i + 1] =False
        for length in range(2,len(s)):
            start = 0
            while start+length<len(s):
                if is_pa[start+1][start+length-1] == True and s[start] == s[start+length]:
                    is_pa[start][start+length] = True
                else:
                    is_pa[start][start+length]= False
                start+=1
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
if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    x = Solution()
    print x.minCut(s)


