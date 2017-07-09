# -*- encoding: utf-8 -*-
#  题目：Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.括号合法不
# 建空stack,建dict,key为右括号,value为左括号,遍历所给括号组,如果在value里(左),就append到stack里,如果在key里(右),就看它对应的value和stack里pop出来的那个一样不.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

if __name__ == "__main__":
    s = '((){[]})'
    v=Solution()
    x = v.isValid(s)

