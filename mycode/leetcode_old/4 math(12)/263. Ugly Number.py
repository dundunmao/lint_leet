# -*- encoding: utf-8 -*-
# 题目：是否只能被2，3，5整除，而不是其他质数的倍数。
# 思路：循环


def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0:
        return False
    if num == 1:
        return True
    u= [2,3,5]
    i=0
    while i<3:
        if num%u[i]==0:
            num = num/u[i]
            i = i
        else:
            i +=1
    if num == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    num=2*3*5*5
    print isUgly(num)