# -*- encoding: utf-8 -*-
# 3级
# 内容:给一个无序组,找到第一个missing的数,run in O(n) time and uses constant space.
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 思路bucket sort,第几个位置就放上数字几,然后遍历一遍,如果那个位置不是那个数,就是missing的
def firstMissingPositive( A):
    n = len(A)
    for index in xrange(n):
        element = A[index]
        while True:
            if element <= 0 or element > n or element == A[element - 1]:#如果element比n大,比0小,或者第几个位置放的是数字几,就break
                break
            A[element - 1], element = element, A[element - 1]  #如果不是,让那个位置就是数字几,然后把那位置原来的数赋给element,下一轮再为element找位置.
    for index in xrange(n):
        if A[index] != index + 1:
            return index + 1    #找到第一个那个位置不是那个数的
    return n + 1
if __name__ =="__main__":
    A = [13,14,11,15]
    print firstMissingPositive( A)