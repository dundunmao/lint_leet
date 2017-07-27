# -*- encoding: utf-8 -*-
# 括号是否合理
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
