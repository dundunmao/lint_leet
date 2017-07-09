# coding:utf-8
# 3级
# 题目:给个数n,问不比n大的非负数里有多少个有1这个digit的,例如n = 13 => 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
# 思路:如果n=xyzdabc,当把d位设为1时,
# (1) xyz * 1000            if d == 0 因为d比1小,所以d后面的数没用了,只能靠他前面的变换,有xyz*1000种变法,这里的1000是指d后面的位数
# (2) xyz * 1000 + abc + 1  if d == 1 abc+1是d后面的数字能变换的个数,+1是因为可以是前后都为0
# (3) xyz * 1000 + 1000     if d > 1  这里面的+1000是说d后面的数不管多大都是1000种变换

def countDigitOne(n):
    if n <= 0:
        return 0
    q, x, ans = n, 1, 0
    while q > 0:
        digit = q % 10  #算d
        q /= 10        #算d前面的数,即xyz
        ans += q * x  #这里算的是d前面的变换,q为xyz,x为1000,就是d后面的位数
        #这块就是算d后面有多少种变换
        if digit == 1:
            ans += n % x + 1 #n % x就是算abc
        elif digit > 1:
            ans += x
        x *= 10
    return ans