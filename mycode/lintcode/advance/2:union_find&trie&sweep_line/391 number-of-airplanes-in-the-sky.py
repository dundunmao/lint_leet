# -*- encoding: utf-8 -*-
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
            timepoints.append((airplane[0], 1))
            timepoints.append((airplane[1], -1))
        print timepoints
        timepoints = sorted(timepoints,cmp = self.sorter)
        # timepoints = sorted(timepoints, key = lambda x:x[0])

        num = 0
        maxi = 0
        for t, status in timepoints: #查看每一个有状态变化的时刻
            num += status
            maxi = max(maxi, num)
        return maxi
if __name__ == "__main__":
    a = [[10,14],[10,15],[10,16],[1,10],[2,10],[3,10],[4,10]]
    s = Solution1()
    print s.countOfAirplanes(a)
