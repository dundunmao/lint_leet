# -*- encoding: utf-8 -*-
# 2级
# 题目：回文正反都能读
# 例如:"A man, a plan, a canal: Panama" is a palindrome."race a car" is not a palindrome.
# 思路：str.isalnum()判断是否为非数字字母的str。两个指针，分别从前和后往前遍历。记住这段code

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        s = s.lower()
        cl = 0
        cr = len(s)-1
        while cl <= cr:
            if not s[cl].isalnum():        # 判断str.isalnum()是为了让出空格
                cl += 1
                continue
            if not s[cr].isalnum():
                cr -= 1
                continue
            if s[cl] != s[cr]:
                return False
            cl += 1
            cr -= 1
        return True
def isPalindrome1(x):
    return x==x[::-1] #不能用这个,因为中间有标点符号和空格
if __name__ == "__main__":
    x = 'a.'
    print isPalindrome1(x)