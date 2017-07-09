# coding:utf-8
# 题目:爬 n 阶的楼梯,每次只能1蹬或2蹬,问一共多少种走法
# 思路:
# n = 1: 走法有: 1 :f_1 = 1
# n = 2: 走法有: 1+1; 2: f_2 = 2
# n = 3: 走法有: 1+1+1; 1+2; 2+1 : f_3 = 3(先走1step,剩下的是f_2,先走2step,剩下的是f_1)
# n = 4: 走法有: 1+1+1+1; 1+1+2; 1+2+1; 2+2; 2+1+1; : f_4 = 5 (先走1step,剩下的是f_3 = 3,先走是2step,剩下的是f_2 = 2)
#f_n = f(n-1)+f(n-2)

# recursive
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n-1)+climbStairs(n-2)

# DP
def climbStairs1(n):
    # f_1 = 1
    # f_2 = 2
    # f_3 = f_1+f_2
    f_pre = 2
    f_pre_pre = 1
    f = 0
    if n == 1:
        return f_pre_pre
    if n ==2:
        return f_pre
    for i in range (3,n+1):
        f = f_pre + f_pre_pre
        f_pre_pre = f_pre
        f_pre = f
    return f

# CCI 8.1 上楼方式可以1step,2step,3step.
# n = 1: 走法有: 1 :f_1 = 1
# n = 2: 走法有: 1+1, 2: f_2 = 2 (先走1step,剩下的是f_1;先走2step;)
# n = 3: 走法有: 1+1+1; 1+2; 2+1; 3: f_3 = 3(先走1step,剩下的是f_2;先走2step,剩下的是f_1;先走3step)
# n = 4: 走法有: (先走1step,剩下的是f_3; 先走2step,剩下的是f_2 = 2; 先走3step,剩下的是f_1)
#f_n = f(n-1)+f(n-2)+f(n-3)

def climbStairs_3step(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return climbStairs_3step(n-1)+climbStairs_3step(n-2) + climbStairs_3step(n-3)

def climbStairs_3step1(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    f_1 = 1
    f_2 = f_1+1
    f_3 = f_1+f_2+1
    f_pre = 4
    f_pre_pre = 2
    f_pre_pre_pre = 1
    f = 0
    for i in range (4,n+1):
        f = f_pre + f_pre_pre +f_pre_pre_pre
        f_pre_pre_pre = f_pre_pre
        f_pre_pre = f_pre
        f_pre = f
    return f

if __name__ == "__main__":
    print climbStairs_3step1(5)
