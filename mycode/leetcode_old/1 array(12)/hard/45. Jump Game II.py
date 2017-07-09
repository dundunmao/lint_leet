# -*- encoding: utf-8 -*-
# 3级
# 内容:一个整数list,你站住第一个位置,你一次能跳到长度就是这个位置的数值.目标是跳最小次数到终点.
# For example,A = [2,3,1,1,4],return 2 (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
# 从第一步开始,记录下这个时候所站位置的范围start和end.然后遍历这个范围,得到下一步能走的最远端==>它就是下一步所站位置的end.而start就是之前位置的end+1
def jump(nums):
    n, start, end, step = len(nums), 0, 0, 0
    while end < n - 1:
        step += 1
        maxend = end + 1
        for i in range(start, end + 1):  #start和end记录这一刻所在的范围
            if i + nums[i] >= n - 1:     #超出范围了,就返回step
                return step
            maxend = max(maxend, i + nums[i])  #这一步能达到的最远位置
        start, end = end + 1, maxend
    return step

if __name__ =="__main__":
    nums = [2,3,1,1,4]
    print jump(nums)