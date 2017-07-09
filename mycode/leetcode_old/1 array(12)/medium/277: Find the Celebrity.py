# coding:utf-8
# 3级
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a functionint findCelebrity(n), your function should minimize the number of calls toknows.
# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return-1.

# 3级
# 题目,n个人,找到名人(人人都认识他,他不认识任何人),你只能问(hi A,你认识B不),问最少的问题.已知一个helper function(bool knows(a,b).

# helper function: def knows(a, b);

def findCelebrity(n):
    l = 0
    r = n-1
    while (l<r):     #双指针,最后找到那个不认识别人的人
        if knows(l,r):
            l+=1
        else:
            r-=1
    for i in range(n):   #确定这个人是不是celebrate
        if i!=l:
            if know(l,i) is True and know(i,l) is False:
                return -1
    return l
