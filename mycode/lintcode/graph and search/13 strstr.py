# coding:utf-8
# 对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# 在面试中我是否需要实现KMP算法？
#
# 不需要，当这种问题出现在面试中时，面试官很可能只是想要测试一下你的基础应用能力。当然你需要先跟面试官确认清楚要怎么实现这个题。
# 样例
# 如果 source = "source" 和 target = "target"，返回 -1。
#
# 如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。
class Solution:
    def strStr(self, source, target):
        # corner case:
        if source is None or target is None:
            return -1
        if source == '' and target == '':
            return 0
        if source == '' and target != '':
            return -1
        if target == '' and source != '':
            return 0
        # main part
        for i in range(len(source)):
            j = 0
            k = i
            while j < range(len(target)):
                if source[k] == target[j]:
                    k += 1
                    j += 1
                else:
                    break
                if j == len(target):
                    return i
        return -1