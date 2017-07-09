# -*- encoding: utf-8 -*-
# 3级
# 内容:安插区间.
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
def insert(intervals, newInterval):
    out = []
    A = sorted(intervals, key=lambda i: i.start)
    i = 0
    while i <len(A):
        if newInterval.start <= A[i].end:
            A[i].end = max(newInterval.end, A[i].end)
            j = i+1
            while j <len(A):
                if A[j].end >= A[i].end:
                    A[i].end = max(A[j].end, A[i].end)

                    out.append(A[i])
                    i = j+1
                    break
                j+=1
        if i<len(A):
            out.append(A[i])
        i+=1
    return out

#别人的方法:
def insert1(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        if i.end < s:
            left += i,
        elif i.start > e:
            right += i,
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [Interval(s, e)] + right

if __name__ =="__main__":
    # a1 = Interval()
    # a1.start = 1
    # a1.end = 2
    # a2 = Interval()
    # a2.start = 3
    # a2.end = 5
    # a3 = Interval()
    # a3.start = 6
    # a3.end = 7
    # a4 = Interval()
    # a4.start = 8
    # a4.end = 10
    # a5 = Interval()
    # a5.start = 12
    # a5.end = 16
    # intervals = [a1,a2,a3,a4,a5]
    # a6 = Interval()
    # a6.start = 5
    # a6.end = 6
    # newInterval = a6
    # insert(intervals, newInterval)
    a1 = Interval()
    a1.start = 1
    a1.end = 5
    a2 = Interval()
    a2.start = 6
    a2.end = 8

    intervals = [a1,a2]
    a6 = Interval()
    a6.start = 5
    a6.end = 6
    newInterval = a6
    insert(intervals, newInterval)