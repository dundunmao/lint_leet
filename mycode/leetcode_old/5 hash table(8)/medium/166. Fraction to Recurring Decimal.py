# -*- encoding: utf-8 -*-
# 3级
# 标签：Array
# 题目:给定两个integer代表分子(numerator)和分母(denominator),找到他们的比in string format.例如
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# 思路: 把每一次的余数都放进一个list里,然后每次都把这个余数乘以10,以便再除一次
# divmod,返回两个数的整除数和余数


def fractionToDecimal(numerator, denominator):
    sign = '-' if numerator * denominator < 0 else ''#考虑负数形式
    n, remainder = divmod(abs(numerator), abs(denominator)) #找到整除数,余数
    result = [sign+str(n), '.']   #把一样一样都放进result这个list里
    stack = []  #存每一次的余数,为的是让每一次的余数*10,好再让分母除一次
    while remainder not in stack: #没有循环的数的时候
        stack.append(remainder)
        n, remainder = divmod(remainder*10, abs(denominator))
        result.append(str(n))

    idx = stack.index(remainder)
    result.insert(idx+2, '(') #在循环的那个数左边插入左括号
    result.append(')')   #在尾巴插入右括号
    return ''.join(result).replace('(0)', '').rstrip('.')  #例如f(6, 3) ''.join(result) == 2.(0);''.join(result).replace('(0)', '').rstrip('.') == 2
if __name__ == "__main__":
    numerator = 10
    denominator = 8
    print fractionToDecimal(numerator, denominator)