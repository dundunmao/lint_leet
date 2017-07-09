# -*- encoding: utf-8 -*-
# 标签：math
# 题目；判断给定的int是不是3的幂
# 思路：用log，看能不能开方
i = 1;
while i * 3 > i:
    i *= 3
print i



import math
def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False
    x = math.log(n,3)
    return abs(round(x) - x) < 0.0000000000001


#或者 1162261467是python2.7里最大的3的幂
    # i = 1;
    # while i * 3 > i:
    #     i *= 3
    # return i
def isPowerOfThree(n):
    if n <= 0:
        return False
    else:
        return 1162261467 % n == 0

if __name__ == "__main__":
    n = 9
    print isPowerOfThree(n)