# coding:utf-8
# 3级
# 题目:找到第n个super ugly number(给k个数的一个质数list primes(升序),SUN就是这些数的乘积,1为特殊SUN).(0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.)
# 例如:primes = [2, 7, 13, 19] of size 4, 前12个SUN就为:[1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32].
# 思路 跟264一样
# prime = [2,7,13,19]
# ugly = [1,2,2*2,2*2*2,7,2*2*2*2,13,2*7, ….]
# ugly[i] = min(prime[j]*ugly[index[j]])  j ~(0,len-1)
# Index = [0,0,0,0]
# i=0
# 2 * ugly[i]
# 7*ugly[i]
# 13*ugly[i]
# prime[j]*ugly[i]

#自己 tle的
def nthSuperUglyNumber(n, primes):
    lenPrime = len(primes)
    indx = [0]*lenPrime             #每一个数对应了primes里那个数的将要去乘的ugly里的index
    ugly = [1]
    while n-1>0:
        want = []
        for j in range(lenPrime):                #把需要添加的列表得出来
            want.append(primes[j]*ugly[indx[j]])     #这个列表就是用[2,7,13,19]分别乘以indx对应点那个数的ugly里对应的那个数
        mini = min(want)                        #找到最小的那个
        indx_prime = want.index(mini)           #找到最小的那个对应的index
        indx[indx_prime]+=1                     #让那个对应的index自加1
        if mini not in ugly:                    #append到ugly里
            ugly.append(mini)
            n-=1
    return ugly[-1]


#网上的,AC的
def nthSuperUglyNumber(self, n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ugly = [1] * n
    i_list = [-1] * len(primes)
    v_list = [1] * len(primes)
    k = 0
    while k < n:
        x = min(v_list)
        ugly[k] = x
        for v in xrange(len(v_list)):
            if x == v_list[v]:
                i_list[v] += 1
                v_list[v] = ugly[i_list[v]] * primes[v]
        k += 1
    return ugly[k-1]
if __name__ == "__main__":
    n = 12
    primes = [2, 7, 13, 19]
    print nthSuperUglyNumber(n, primes)