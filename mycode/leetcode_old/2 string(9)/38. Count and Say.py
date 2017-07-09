# -*- encoding: utf-8 -*-
# 2级
# 题目：The count-and-say sequence就是1, 11, 21, 1211, 111221, ... 找到第n个数.
# 其中：1 is read off as "one 1" or 11.
#     11 is read off as "two 1s" or 21.
#     21 is read off as "one 2, then one 1" or 1211.

# 思路：

def countAndSay(n):
    if n == 1:
        return '1'
    x = '1'
    while n > 1:
        x = count(x)
        n -= 1
    return x

def count(x):
    m = list(x)
    ans =[]
    m.append(None)
    i , j = 0 , 0
    while i < len(m)-1:
        j += 1
        if m[j] != m[i]:
            ans += [ j-i, m[i] ]   #j-i是个数,
            i = j                  #再往下走
    return ''.join(str(s) for s in ans) #合并
if __name__ == "__main__":
    print count('11')
    n = 4

    print countAndSay(n)

