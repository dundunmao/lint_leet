# -*- encoding: utf-8 -*-
# 3级
# 题目:给两个strings形式的number,返回string形式的两个数之积.
# 思路:两个数相乘,一位一位的乘,列竖式的方法
def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))
    pos = len(product)-1

    for n1 in reversed(num1):  #倒着遍历
        tempPos = pos
        for n2 in reversed(num2): #倒着遍历
            product[tempPos] += int(n1) * int(n2)  #最后两位相乘
            product[tempPos-1] += product[tempPos]/10 #把十位数的数放在倒数第二个index上
            product[tempPos] %= 10          #倒数第一个index上直留个位数
            tempPos -= 1
        pos -= 1
    pt = 0  #下面是算这里面有几个0
    while pt < len(product)-1 and product[pt] == 0:
        pt += 1
    return ''.join(map(str, product[pt:])) #除了0之外的数变成string,在join到一起