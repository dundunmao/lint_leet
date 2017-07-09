# -*- encoding: utf-8 -*-
# 题目:convert a string to an integer.
# 思路:要去除前后的空格(.strip),要留下前面的正负号,如果有不是数字的element(用.isdigit检查),return 0

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    str = str.strip()
    if len(str) == 0:
        return 0
    tmp = "0"
    result = 0
    i = 0
    if str[0] in "+-":
        tmp = str[0]
        i = 1
    MAX_INT = 2147483647
    MIN_INT = -2147483648
    for i in xrange(i, len(str)):
        if str[i].isdigit():
            tmp += str[i]
        else:
            break
    if len(tmp) > 1:
        result = int(tmp)
    if result > MAX_INT > 0:
        return MAX_INT
    elif result < MIN_INT < 0:
        return MIN_INT
    else:
        return result

if __name__ == "__main__":
    str = "123"
    print myAtoi(str)