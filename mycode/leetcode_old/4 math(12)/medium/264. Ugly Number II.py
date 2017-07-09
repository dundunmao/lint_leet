# coding:utf-8
# 3级
# 题目: 找到第n个ugly number(2,3,5的倍数,1也是,是特殊情况)例如1, 2, 3, 4, 5, 6, 8, 9, 10, 12 前10个 ugly numbers
# 思路: 这些数分别是,1个2,2个2,3个2,4个2,5个2....1个3,2个3,3个3,4个3....1个5,2个5,(其中个数必须是曾经出现过的,不如不能有7个2).谁小先往队列ugly里append谁.
#     u2, u3, u5就是这些个数,i2,i3,i5是找到u的index.每个index用完,就继续自加(+=1)
def nthUglyNumber(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    while n > 1:
        u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
        umin = min((u2, u3, u5))
        if umin == u2:
            i2 += 1
        if umin == u3:
            i3 += 1
        if umin == u5:
            i5 += 1
        ugly.append(umin)
        n -= 1
    return ugly[-1]


if __name__ == "__main__":
    print nthUglyNumber(10)