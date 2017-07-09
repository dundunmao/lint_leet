# -*- encoding: utf-8 -*-
# 3级
# 内容:合并区间
# 例如Given [1,3],[2,6],[8,10],[15,18],return [1,6],[8,10],[15,18].
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    out = []
    for i in sorted(intervals, key=lambda i: i.start):  #按i.start排序
        if out and i.start <= out[-1].end:   #如果前一个的尾 > 后一个的头,就说明有overlap. 就out里的最后一个数的end > i.start
            out[-1].end = max(out[-1].end, i.end)   #前一个的尾就为两个尾巴里大的那个
        else:
            out += i,    #把当前这个加入out
    return out

if __name__ =="__main__":
    a1 = Interval()
    a1.start = 1
    a1.end = 3
    a2 = Interval()
    a2.start = 2
    a2.end = 6
    a3 = Interval()
    a3.start = 8
    a3.end = 10
    a4 = Interval()
    a4.start = 15
    a4.end = 18
    intervals = [a1,a2,a3,a4]
    merge(intervals)