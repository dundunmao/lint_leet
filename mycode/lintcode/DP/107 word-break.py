# coding=utf-8

# 给出一个字符串s和一个词典，判断字符串s是否可以被空格切分成一个或多个出现在字典中的单词。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出
#
# s = "lintcode"
#
# dict = ["lint","code"]
#
# 返回 true 因为"lintcode"可以被空格切分成"lint code"
class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict


    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0 and len(s) == 0:
            return True
        if s is None or len(s) == 0 or len(dict) == 0:
            return False
        can = [False for i in range(len(s)+1)]
        can[0] = True
        max_len = max(dict)
        for i in range(1,len(s)+1):
            for j in range(1,min(i,max_len)+1):
                if not can[i - j]:
                    continue
                word = s[(i-j):i]
                if word in dict:
                    can[i] = True
                    break
        return can[len(s)]


# time limit exceed

class Solution1:
    # @param s: A string s
    # @param dict: A dictionary of words dict

    def wordBreak(self, s, dict):
        if len(dict) == 0 and len(s) == 0:
            return True
        if s is None or len(s) == 0 or len(dict) == 0  :
            return False
        n = len(s)
        f = [False for i in range(n)]
        for k in range(n):
            word = s[0:k+1]
            if word in dict:
                f[k] = True

        for i in range(1,n):
            for j in range(0,i):
                word = s[j+1:i+1]
                if word in dict and f[j]:
                    f[i] = True
        return f[n-1]

#尽量优化版,仍超时;第一个不超时的办法,是j从后往前遍历
class Solution3:
    # @param s: A string s
    # @param dict: A dictionary of words dict

    def wordBreak(self, s, dict):
        if len(dict) == 0 and len(s) == 0:
            return True
        if s is None or len(s) == 0 or len(dict) == 0:
            return False
        n = len(s)
        max_len = max([len(word) for word in dict])
        f = [False for i in range(n)]
        for k in range(n):
            word = s[0:k + 1]
            if word in dict:
                f[k] = True

        for i in range(1, n):
            for j in range(0, i):
                if f[j]:
                    word = s[j + 1:i + 1]
                    if len(word) <= max_len:
                        if word in dict:
                            f[i] = True
                            break
if __name__ == "__main__":
    s = "a"
    dict = ["a"]
    x = Solution1()
    print x.wordBreak(s,dict)