__author__ = 'eva'

def step_way(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    total_ways = step_way(n -1) + step_way(n - 2) + step_way(n - 3)
    return total_ways

def sub_set(li):
    list_total = []
    for i in range(0,len(li)):
        if len(li)<=1:
            list_total.append(li[0])
            return
        a = li[i]
        list_total.append(a)

        li.pop(i)
        c = sub_set(li)
        list_total.append(c)
    return list_total

import itertools


def comb(list1):

    list2 = []

    for i in range(1,len(list1)+1):
        iter = itertools.combinations(list1,i)
        list2.append(list(iter))
    list3 = []
    for i in range(0,len(list2)):
        for j in range(0,len(list2[i])):
            list3.append(list2[i][j])
    return list3

def c(n,m,out):
    if(m==0):
        return 1
    x=n
    while x>=m:
        out.append(x)
        if(c(x-1,m-1,out)):
            print out
        out.pop()
        x-=1
    return 0











if __name__=='__main__':
    # print step_way(1), step_way(2), step_way(3), step_way(4), step_way(5), step_way(6)

    l = ['a','b','c']
    list1 = 'abcdefghijklm'
    # print sub_set(l)
    new_list = comb(list1)

    print len(new_list)

    c(7,4,out=[])

    print out