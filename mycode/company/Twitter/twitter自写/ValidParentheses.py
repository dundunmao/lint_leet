# -*- encoding: utf-8 -*-
# 括号是否valid
def ValidParentheses(s):

    hash = {')':'(','}':'{',']':'['}
    if s == '':
        return True
    stack = []
    for i in range(len(s)):
        if s[i] in hash:
            if hash[s[i]] != stack.pop():
                return False
        elif s[i] in hash.values():
            stack.append(s[i])
    return True


if __name__ == '__main__':
    s = "()[]{}"
    t = "([)]"

    print ValidParentheses(s)