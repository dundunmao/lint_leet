# -*- encoding: utf-8 -*-
# 3.5级
# 题目: 给出表达式的string,return结果.例如"3+2*2" = 7; " 3/2 " = 1; " 3+5 / 2 " = 5
# 思路:  only need 2 variable (a,b) to save the data.
#       if operator is '*' or '/', use b to calculate , then save it to b.
#       if operator is '+' or '-', then a = a +/- b b = new_number
#
# 遍历到的是运算符=>如果之前(op)没有运算符,num存进a里,
#                 否则如果之前是+- =>如果再之前(preop)没有运算符,num存进b里
#                                    否则a = a+-b; b=num
#                                    同时,preop更新为op
#                 否则如果之前是*/ =>如果再之前(preop)没有运算符,a=a*/num
#                                     否则:b=b*/num
#                 同时:op更新为这一轮的符号,num清空
# 遍历到的是数字,就存进num里,如果级个数字之间没有运算符,就需要乘以10
# 最最后返回a+-b
def calculate(s):
    s += '#'
    num = 0
    a = b = None
    preop = op = None
    for c in s:
        if c in ('+','-','*','/','#'):
            if op is None:
                a = num
            elif op in ('+','-'):
                if preop is None:
                    b = num
                else:
                    a = a + b if preop == '+' else a - b
                    b = num
                preop = op
            else:
                if preop is None:
                    a = a * num if op == '*' else a / num
                else:
                    b = b * num if op == '*' else b / num
            op = c
            num = 0
        elif c != ' ':
            num = num * 10 + int(c)  #num里存每次遍历的数字,如果级个数字之间没有运算符,就需要乘以10.
    if preop is None:
        return a
    return a + b if preop == '+' else a - b


def calculate1(self, s):
    if not s:
        return "0"
    stack, num, sign = [], 0, "+"
    for i in xrange(len(s)):
        if s[i].isdigit():
            num = num*10+ord(s[i])-ord("0")
        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
            if sign == "-":
                stack.append(-num)
            elif sign == "+":
                stack.append(num)
            elif sign == "*":
                stack.append(stack.pop()*num)
            else:
                tmp = stack.pop()
                if tmp//num < 0 and tmp%num != 0:
                    stack.append(tmp//num+1)
                else:
                    stack.append(tmp//num)
            sign = s[i]
            num = 0
    return sum(stack)





if __name__ == "__main__":
    s = "3+2*2-9"
    print calculate(s)