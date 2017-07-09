# -*- encoding: utf-8 -*-
# 2级,同228
# 题目Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.
#         给定一个sorted integer array, range是[lower, upper]找到 missing ranges.
# 例如 given [0, 1, 3, 50, 75] , lower = 0 and upper = 99, return  ["2", "4->49", "51->74", "76->99"].
def findMissingRanges(list,lower,upper):
    result = []
    l = lower
    r = 0
    for i in range(0,len(list)):
        if i == 0 and l<list[i]:    #把头,且lower小于第一个数时
            result.append(printRange(l,list[i]-1))
            print result
        if i!=0 and list[i]-1!=list[i-1]:   #中间的情况:当数不挨着时
            l = list[i-1]+1
            r = list[i]-1
            result.append(printRange(l,r))
            print result
        if i == len(list)-1 and i+1<upper:   #把尾,且最后一个数小于upper时
            result.append(printRange(list[len(list)-1]+1,upper))
            print result
    return  result
def printRange(l, r):  #板式
    if l == r:
        return str(l)
    else:
        return str(l) + "->" + str(r)
if __name__ =="__main__":
    list = [1, 3, 50, 75]
    lower = 0
    upper = 99
    print findMissingRanges(list,lower,upper)