# -*- encoding: utf-8 -*-
# 题目：n以内有几个质数(<n)
# 思路：从2开始，2的倍数都不是质数，然后3的倍数，然后往下依次。。。

def countPrimes( n):
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in xrange(2, n):
            if res[i] == True:
                for j in xrange(2, (n-1)//i+1):  #比如这里是2的倍数,i就为1,(i+1)就是2,(n-1)就是最后一个数的index,就是为了不超界
                    res[i*j] = False # i的倍数为False
        return sum(res),res

if __name__ == "__main__":
    print countPrimes(5)
