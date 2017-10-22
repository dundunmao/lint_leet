# -*- encoding: utf-8 -*-
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.
#

# 思路，在每个状态变化的点，做数量的加减，要先减后加。
#
# 例如：[[0, 30],[5, 10],[15, 20]]
# 开始存入intervals：[(0, 1), (30, -1), (5, 1), (10, -1), (15, 1), (20, -1)]表示了每个关键时间点是开还是关
# 按时间sort，如果时间相同就按关或开roomsort，sort之后为：
# [(0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (30, -1)]
# 然后从头遍历，就是去每一个关键时间点查看，然后累加1或-1找最大的状态
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def sorter(self, x, y):
        if x[0] != y[0]:
            return x[0] - y[0]
        return x[1] - y[1]
    def countOfAirplanes(self, airplanes):
        timepoints = []
        for airplane in airplanes:
            timepoints.append((airplane.start, 1))
            timepoints.append((airplane.end, -1))

        timepoints = sorted(timepoints, cmp=self.sorter)

        sum, most = 0, 0
        for t, delta in timepoints:
            sum += delta
            most = max(most, sum)
        return most



class Solution1:
    # @param airplanes, a list of Interval
    # @return an integer
    def sorter(self, x, y): #先落再升
        if x[0] != y[0]:
            print x[0] - y[0]
            return x[0] - y[0]
        print x[1] - y[1]
        return x[1] - y[1]
    def countOfAirplanes(self, airplanes):
        timepoints = []
        for airplane in airplanes:
            timepoints.append((airplane[0], 1))  #（某个时间点，开一个room）
            timepoints.append((airplane[1], -1)) #（某个时间点，关一个room）
        timepoints = sorted(timepoints,cmp = self.sorter)
        # timepoints = sorted(timepoints, key = lambda x:x[0])

        num = 0
        maxi = 0
        for t, status in timepoints: #查看每一个有状态变化的时刻
            num += status
            maxi = max(maxi, num)
        return maxi
if __name__ == "__main__":
    a = [[0, 30],[5, 10],[15, 20]]
    s = Solution1()
    print s.countOfAirplanes(a)