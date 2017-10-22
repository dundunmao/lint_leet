# -*- encoding: utf-8 -*-

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        interv_sort = sorted(intervals, key =lambda x:x.start)  #按start time排序
        for i in range(len(interv_sort)-1):       #遍历看当前的end在不在下一个start的后面
            if interv_sort[i].end > interv_sort[i+1].start:
                return False
        return True