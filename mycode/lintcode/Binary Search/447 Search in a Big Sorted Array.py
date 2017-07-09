# coding:utf-8
# 给一个按照升序排序的正整数数组。这个数组很大以至于你只能通过固定的接口 ArrayReader.get(k) 来访问第k个数。(或者C++里是ArrayReader->get(k))，并且你也没有办法得知这个数组有多大。找到给出的整数target第一次出现的位置。你的算法需要在O(logk)的时间复杂度内完成，k为target第一次出现的位置的下标。
#
# 如果找不到target，返回-1。
#
#  注意事项
#
# 如果你访问了 ArrayReader 中一个不可访问的下标（比如越界），ArrayReader 会返回 MAXINT = 2,147,483,647。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出 [1, 3, 6, 9, 21, ...], and target = 3, return 1.
#
# 给出 [1, 3, 6, 9, 21, ...], and target = 4, return -1.


"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # if there is no number on that index, return -1
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if reader is None:
            return -1
        if target is None:
            return -1
        # get the length
        end = 1
        while reader.get(end-1) != -1:
            if reader.get(end-1)  < target:
                end = end*2
            else:
                break
        start = 0
        while start + 1 < end:
            mid = start + (end - start) / 2
            value_mid = reader.get(mid)
            if value_mid >= target or value_mid == -1:
                end = mid
            elif value_mid < target:
                start = mid
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1