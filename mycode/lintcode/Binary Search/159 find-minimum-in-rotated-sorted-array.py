# coding:utf-8
# 假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。
#
# 你需要找到其中最小的元素。
#
# 你可以假设数组中不存在重复的元素。
#
#  注意事项
#
# You may assume no duplicate exists in the array.
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出[4,5,6,7,0,1,2]  返回 0
class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if num is None or len(num) == 0:
            return False
        start = 0
        end = len(num) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if num[mid] > num[end]:
                start = mid
            else:
                end = mid
        if num[start] < num[end]:
            return num[start]
        else:
            return num[end]