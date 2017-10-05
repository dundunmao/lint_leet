# -*- encoding: utf-8 -*-
# 括号是否合理

# 方法一：
# 建一个空stack，建个hash={"]":"[", "}":"{", ")":"("}看到出左边的在value，右边的在key里，
# 遍历string，遇到左边，就压入stack，如果是右半，就看跟栈顶的配不配对，配对，就把栈顶的pop出去，不配对，就false。

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values(): #如果是左半，就压入栈
                stack.append(char)
            elif char in dict.keys(): #如果是右半
                if stack == [] or dict[char] != stack.pop():#如果栈空，就false；如果本轮的char对应的左半不是栈pop出来的那个，也false。如果是，就pop并进入下一轮
                    return False
        return stack == []

    # 方法二：


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True

        if n % 2 != 0:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')

        if s == '':
            return True
        else:
            return False


if __name__ == "__main__":
    str = '()())()'
    s = Solution()
    print s.isValid(str)