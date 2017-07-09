
# -*- encoding: utf-8 -*-
# 2级
# 内容：数字按digit转成nums，在这个数字上加1，再转成list
# 思路：乘以和除以10的幂数。
def plusOne(digits):

    num = 0
    for i in range(0,len(digits)):
        num +=10**(len(digits)-1-i)*digits[i]

    num = num+1
    out = []
    l = len(str(num))
    for j in range(0,l):
        power = 10**(l-j-1)
        out.append(num/power)
        num = num%power
    return out

#方法2:
def plusOne1(digits):
        sum = 0
        for i in range(len(digits)):
            sum += digits[-(i+1)]*(10**i) #末位乘以10的n次方
        sum +=1
        return [int(i) for i in str(sum)] #遍历str，依次往list里加




        sum = 0
        for i in range(len):
            sum +=digits[-1-i]*10**1
        sum +=1
        return [int(str) for str in str(sum)]
if __name__ =="__main__":
    nums = [1,0,1]

    print plusOne1(nums)