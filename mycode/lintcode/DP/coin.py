
# -*- encoding: utf-8 -*-
# 给三种硬币[1,2,3],给总额n.问几种方法

def coin(n):
    f = [0 for i in range(n+1)]
    f[1] = 1
    f[2] = 2
    f[3] = 3

    for i in range(4,n+1):
        f[i] = f[i-1]+f[i-2]+f[i-3]
    return f[n]

if __name__ == "__main__":
    a = 5
    print coin(a)
