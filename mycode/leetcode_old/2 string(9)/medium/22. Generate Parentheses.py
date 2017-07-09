# -*- encoding: utf-8 -*-
# 3级 背下来
# 题目:给一个数n,返回n个括号的组合,例如n=3,return "((()))", "(()())", "(())()", "()(())", "()()()"
# 思路: recursive.

def generateParenthesis(n):
    def generate(p, left, right, parens=[]):
        if left:
            generate(p + '(', left-1, right) #如果有左,就往p里加左,
        if right > left:
            generate(p + ')', left, right-1) #如果右比左多,就往p里加右
        if not right:
            parens += p,                    #如果没有右了,这一轮就结束,p就成了一个, 往parents里加p
        return parens
    return generate('', n, n)
if __name__ == '__main__':
    n = 2
    print generateParenthesis(n)
